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
parser.add_argument('cfgfile', type=str,
                    help='Config file with replace rules')
parser.add_argument('textfile', type=str, help='Text file to process')
args = parser.parse_args()


# init
#
cfgdict = {}
cfgkeys = '['
textoutlist = []


def replaceFunction(matchobj):
    global replacecounter
    replacecounter += 1
    return cfgdict[str(matchobj.group(0))]


# processing
#
try:
    with open(args.cfgfile, 'r', encoding='utf-8', errors='replace') as cfg, \
         open(args.textfile, 'r', encoding='utf-8', errors='replace') as txt:

        # building dictionary of replascement pairs from config file
        #
        for cfgline in cfg:
            match = re.search('(\S+)=(\S+)', cfgline.strip())
            if match:
                cfgdict.update({str(match.group(1)).strip():
                                str(match.group(2)).strip()})

        if len(cfgdict) == 0:
            print('Error: empty config set')
            quit()

        # config keys for RegEx replace function
        #
        cfgkeys += ''.join(cfgdict.keys())
        cfgkeys += ']{1}'

        # processing income data,
        # appending count marks (replacecounter) and
        # filling list of unsorted results
        #
        for line in txt:
            replacecounter = 0
            textline = re.sub(cfgkeys, replaceFunction, line).rstrip()
            textoutlist.append(str(replacecounter).zfill(10) + textline)

except IOError as e:
    print('Error ' + str(e))
    quit()

# sorting list
# and printing results, cleared from count marks
#
if (len(textoutlist) > 0):
    for outLine in sorted(textoutlist, reverse=True):
        print(outLine[10:])
else:
    print('Empty result.')
