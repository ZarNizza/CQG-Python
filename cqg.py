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

import re
import argparse
import os.path

class TextProcessor:
    # init
    cfg_dict = {}
    cfg_keys = '['
    text_out_list = []
    replace_counter = 0

    def replace_function(self, match_obj):
    # increment counter and return symbol for replacement
        self.replace_counter += 1
        return self.cfg_dict[str(match_obj.group(0))]

    def load_config(self, cfg_file_name):
    # preparing dictionary and keys list
        try:
            with open(cfg_file_name, 'r', encoding='utf-8', errors='replace') as c_file:

                # creating dictionary of replacement pairs from config file
                for c_line in c_file:
                    match = re.search('(\S+)=(\S+)', c_line.strip())
                    if match:
                        self.cfg_dict.update({str(match.group(1)).strip():
                                        str(match.group(2)).strip()})

                if not len(self.cfg_dict):
                    print('Error: empty config set')
                    quit()

                # set config keys for RegEx replace function
                self.cfg_keys += ''.join(self.cfg_dict.keys())
                self.cfg_keys += ']{1}'

        except IOError as e:
            print('Error ' + str(e))
            quit()

    def replace_text(self, txt_file_name):
    # processing
        try:
            with open(txt_file_name, 'r', encoding='utf-8', errors='replace') as t_file:

                # prevent useless work if the text file is empty
                # (it's existence verified by Try/With/Open operation)
                if not os.path.getsize(txt_file_name):
                    print('Error: empty text file')
                    quit()

                # RegEx search&replacing,
                # add count mark (replace_counter), and
                # appending the list of unsorted results
                for t_line in t_file:
                    self.replace_counter = 0
                    text_line = re.sub(self.cfg_keys, self.replace_function, t_line).rstrip()
                    self.text_out_list.append(str(self.replace_counter).zfill(10) + text_line)

                # sorting list
                self.text_out_list.sort(reverse=True)

        except IOError as e:
            print('Error ' + str(e))
            quit()

    def prn(self):
    # printing results, cleared from count marks
        for out_line in self.text_out_list:
            print(out_line[10:])


# getting Config and Text files names from command line arguments
description_text = '''This program get a list of symbol pairs from a Configuration file,
    and replace value1 by value2 for all matches in a given Text file.
    Then sort changed lines by the total number of symbols replaced,
    starting from the most changed line and output resulting text to console.
    Names of both files are passed as command line arguments.'''
parser = argparse.ArgumentParser(description=description_text)
parser.add_argument('cfg_file_name', type=str,
                    help='Config file with replace rules')
parser.add_argument('txt_file_name', type=str,
                    help='Text file to process')
args = parser.parse_args()

tp = TextProcessor()
tp.load_config(args.cfg_file_name)
tp.replace_text(args.txt_file_name)
tp.prn()