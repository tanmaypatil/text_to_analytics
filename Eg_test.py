from fileRead import findMarker,checkPacks,getPackInfo
from packs import packs
# Execute pytest like Shell
# python -m pytest test_file.py

def test_find_sched():
    line = 'P2G_SCHED	 Env Details	  	 Operational KPIs	 Engineering KPIs	 Soap Job';
    val = findMarker(line,'P2G_SCHED')
    assert val != None
    

def test_checkPackPresence():
    index = packs.index('2GO_FEDNOW')
    assert index > 0
    
def test_checkPackFound():
    line = '''1	 2GO_SWIFT	 PRD_EG_4621_2GO01	 Rajendra Joshi	 WLS	 Azure	  	 100%	  	 64%	 -	 1329	 1329	 1338	 Not Executed 	2.2.0-alpha_b81'''
    result = checkPacks(packs,line)
    assert result == 'found'
    
def test_checkPackInfo():
    line = '''1	 2GO_SWIFT	 PRD_EG_4621_2GO01	 Rajendra Joshi	 WLS	 Azure	  	 100%	  	 64%	 -	 1329	 1329	 1338	 Not Executed 	2.2.0-alpha_b81'''
    result = getPackInfo(packs,line)
    assert result["packName"] == '2GO_SWIFT'
    assert result['passPcnt'] == '64%'