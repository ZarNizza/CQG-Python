import  re, argparse

# getting Config and Text files names from command line arguments
#
descriptionText = 'This program get a list of symbol pairs from a Configuration file,\nand replace value1 by value2 for all matches in a given Text file.\nThen sort changed lines by the total number of symbols replaced, starting from the most changed line and\noutput resulting text to console.\nNames of both files are passed as command line arguments'
parser = argparse.ArgumentParser(description = descriptionText)
parser.add_argument('confFile', type = str, help = 'Config file with replace rules')
parser.add_argument('textFile', type = str, help = 'Text file to process')
args = parser.parse_args()


# init variables
#
cfgDict = {}
cfgKeys = '['
txtOutList = []
replaceCounter = 0

with open(args.confFile, 'r', encoding='utf-8', errors='replace') as cfg, open(args.textFile, 'r', encoding='utf-8', errors='replace') as txt:

  # building Dictionary of replascement pairs from config file
  #
  for cfgLine in cfg:
    match = re.search('(\S+)=(\S+)', cfgLine.strip())
    if match:
      cfgDict.update({str(match.group(1)).strip() : str(match.group(2)).strip()})
  cfgKeys += ''.join(cfgDict.keys())
  cfgKeys += ']{1}'

  # defining regex replace function
  #
  def replaceFunction(matchObj):
    global replaceCounter
    replaceCounter += 1
    return cfgDict[str(matchObj.group(0))]

  # processing income data,
  # appending count marks (replaceCounter) and
  # filling List of unsorted results
  #
  for line in txt:
    replaceCounter = 0
    txtLine = re.sub(cfgKeys,replaceFunction,line).rstrip()
    txtOutList.append(str(replaceCounter).zfill(10) + txtLine)

# sorting list
# and printing results, cleared from count marks
#
if(len(txtOutList) > 0):
  for outLine in sorted(txtOutList, reverse = True):
    print(outLine[10:])
else:
  print('Empty result.')