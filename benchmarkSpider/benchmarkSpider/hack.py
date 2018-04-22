import json
import sys
from scanner import Scanner
from utility import *
import time


hackHub = {}
data = []
data_path = path+'/result/url_result.json'

time.sleep(1)

try:
    with open(data_path,'r') as f:
        try: 
            for line in f.readlines():
                data.append((str(json.loads(line)['link'])))
        except ValueError:
            print 'fail to load url file'
            
except IOError:
    print 'fail to open url json file'

def updateHackHub(obj):
    category = obj.category
    scope = obj.vul_info
    if(DT in hackHub):
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
    for link in data:
        hack = Scanner(link)
        hack.scan()
        if not hack.safe:
            updateHackHub(hack)
            saveScript(hack,len(hackHub[hack.category]['result'][start_url]))
    saveScope()
        
