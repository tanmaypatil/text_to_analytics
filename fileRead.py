
import re
def readFile(fileName):
   with open(fileName) as reader:
      for line in reader :
        print(line)

#readFile('EXT Evergreen Automation Status  2GO - 09.08.txt')

def findMarker(line,marker) :
   regStr = "^" + marker + ".*$"
   match = re.search(regStr,line) 
   if(match):
       print(match.group())
       return match
   else :
       print('not found P2G_SCHED')
       
#fileName ='EXT Evergreen Automation Status  2GO - 23.08.txt'
'''
def readPackStatus(fileName,marker):
    markerFound = 0 
    with open(fileName) as reader:
      for line in reader :
        if ( markerFound == 0) :
          # find the line with marker e.g P2G_SCHED
          marker = findMarker(line,marker)
          if ( marker ):
            markerFound = 1  
        else:
          # to check if we find the pack
'''

def checkPacks(packs,line):
  pattern = ''
  for pack in packs:
    pattern = pattern + "|" + pack
  # check for pack in line
  match = re.search(pattern,line)
  if(match):
        return 'found'
  else :
        return None
      
def getPackInfo(packs,line):
      packDict = {}
      if(checkPacks(packs,line) == 'found'):
            tokens = line.split(' ')
            packDict["packName"] = tokens[1].strip('\t') 
            packDict['envName'] = tokens[2].strip('\t')
            packDict['passPcnt'] = tokens[12].strip('\t')
            print(tokens,",")
            return packDict;
      else :
            return None
            

       
               
              
    
      
          
