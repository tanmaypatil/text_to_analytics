from packs import packs
import re
def readFile(fileName):
   with open(fileName) as reader:
      for line in reader :
        print(line)

#readFile('EXT Evergreen Automation Status  2GO - 09.08.txt')

def findMarker(line,marker) :
   regStr =   marker + ".*$"
   match = re.search(regStr,line) 
   if(match):
       print(match.group())
       return match
   else :
       print('not found P2G_SCHED')
       
#fileName ='EXT Evergreen Automation Status  2GO - 23.08.txt'


#check pack such 
def isPackPresentInReport(packs,line):
  pattern = ''
  for pack in packs:
    pattern = pattern + pack + "|"
  pattern = pattern.strip("|")
  # check for pack in line
  match = re.search(pattern,line)
  if(match):
        return 'found'
  else :
        return None
      
def getPackInfo(packs,line):
      packDict = {}
      if(isPackPresentInReport(packs,line) == 'found'):
            tokens = line.split(' ')
            packDict["packName"] = tokens[1].strip('\t') 
            packDict['envName'] = tokens[2].strip('\t')
            packDict['passPcnt'] = tokens[12].strip('\t')
            packDict['executedTest'] = tokens[14].strip('\t')
            print(tokens,",")
            return packDict;
      else :
            return None
          
# read all packs run stats and store it in a list     
def readAllPacksStats(fileName : str,marker : str):
    allPacks = []
    markerFound = "notFound" 
    packsCount = 0 
    finalLine = ''
    with open(fileName) as reader:
      for line in reader :
        if ( markerFound == "notFound") :
          # find the line with marker e.g P2G_SCHED
          markerFound = findMarker(line,marker) 
        else:
          # to check if we find the pack
         packInfo = getPackInfo(packs,line)
         if (packInfo):
          allPacks.append(packInfo)
          packsCount =  packsCount + 1
          # If you find all packs , return
          if ( len(packs) == packsCount):
            break 
    
    return allPacks

       
               
              
    
      
          
