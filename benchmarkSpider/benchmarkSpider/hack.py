import json
import sys
from scanner import Scanner
from utility import *

hackHub = {}
data = {}
try:
    with open(path+'/result/url_result.json','w') as f:
        try: 
            data = json.load(f)
        except ValueError:
            print 'fail to load json file'
            
except IOError:
    print 'fail to open url json file'

def updateHackHub(obj):
    category = obj.category
    scope = obj.vul_info
    if(hackHub[category]):
        hackHub[category]['result'][start_url]+=scope['result'][start_url]
    else:
        hackHub[category]=scope

def saveScript(hack,id):
    cate_str = '_'.join(hack.category.split(' '))
    script_name = 'result/'+cate_str+'_attack'+str(id)+'.sh'
    with open(script_name, 'w') as f:
        f.write(hack.attack_script)

def saveScope():
    for key in hackHub.keys():
        cate_str = '_'.join(key.split(' '))
        file_name = 'result/'+cate_str+'_scope.json'
        scope = hackHub[key]
        with open(file_name,'w+') as f:
            json.dump(scope,f)
    
if data:
    links = [d['link'] for d in data]
    for link in data:
        hack = Scanner(link)
        if not hack.safe:
            updateHackHub(hack)
            savescript(hack,len(hackHub[hack.category]['result'][start_url]))
    saveScope()
        
