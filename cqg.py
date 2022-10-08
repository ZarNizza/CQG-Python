# IMHO, nice & fast, resourse-saving solution is:
# - to use RegEx for search-and-replace operation,
# - apply sort "in-place" list.sort() method.
#
# For this purpose:
# - create dictionary of replacement pairs from config file,
# - get config keys from dictionary for RegEx replace function,
# - count number of replacements in replace function,
# - add current result number of replacements into current text line as prefix,
# - discard it at the final print.
#

import re
import argparse

# getting Config and Text files names from command line arguments
#
descriptiontext = 'This program get a list of symbol pairs from a Configuration file, \
    and replace value1 by value2 for all matches in a given Text file. \
    Then sort changed lines by the total number of symbols replaced, \
    starting from the most changed line and output resulting text to console. \
    Names of both files are passed as command line arguments.'
parser = argparse.ArgumentParser(description=descriptiontext)
parser.add_argument('cfg_file', type=str,
                    help='Config file with replace rules')
parser.add_argument('text_file', type=str, help='Text file to process')
args = parser.parse_args()


# init
#
cfg_dict = {}
cfg_keys = '['
text_out_list = []

# replace function:
# increment counter and
# return symbol for replacement
#
def replace_function(match_obj):
    global replace_counter
    replace_counter += 1
    return cfg_dict[str(match_obj.group(0))]


# processing
#
try:
    with open(args.cfg_file, 'r', encoding='utf-8', errors='replace') as c_file, \
         open(args.text_file, 'r', encoding='utf-8', errors='replace') as t_file:

        # creating dictionary of replacement pairs from config file
        #
        for c_line in c_file:
            match = re.search('(\S+)=(\S+)', c_line.strip())
            if match:
                cfg_dict.update({str(match.group(1)).strip():
                                str(match.group(2)).strip()})

        if len(cfg_dict) == 0:
            print('Error: empty config set')
            quit()

        # set config keys for RegEx replace function
        #
        cfg_keys += ''.join(cfg_dict.keys())
        cfg_keys += ']{1}'

        # RegEx search&replacing,
        # add count mark (replace_counter), and
        # appending the list of unsorted results
        #
        for t_line in t_file:
            replace_counter = 0
            text_line = re.sub(cfg_keys, replace_function, t_line).rstrip()
            text_out_list.append(str(replace_counter).zfill(10) + text_line)

except IOError as e:
    print('Error ' + str(e))
    quit()

# sorting list,
# and printing results, cleared from count marks
#
if (len(text_out_list) > 0):
    text_out_list.sort()
    for out_line in text_out_list:
        print(out_line[10:])
else:
    print('Empty result.')
