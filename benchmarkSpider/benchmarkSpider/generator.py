from utility import *
import json

def genDT(endpoint,params,method):
    scope = {
        'class':DT,
        'result':{
            start_url: [
                {
                    'endpoint': endpoint,
                    'params': params,
                    'method': 'GET'
                }
            ]
        }
    }    
    scope_name = path + '/result/DT_scope.json'
        
    script = 'curl '+start_url+endpoint+'?'
    keys = params.keys()
    values = params.values()
    pair = [keys[i]+'='+values[i] for i in range(len(keys))]
    evil_param = '&'.join(pair)
    script+=evil_param
    script_name = path+'/result/DT_script.sh'
    return scope, script

def genSI():
    pass

def genSCI():
    pass

def genSSCI():
    pass

def genCSRF():
    pass

def genOR():
    pass

render = {
    DT: genDT,
    SI: genSI,
    CSRF: genCSRF,
    OR: genOR,
    SSCI: genSSCI,
    SCI: genSCI
}

class generator(object):
    def __init__(self,category):
        self.scope = {}
        self.category = category
        self.cate_str = '_'.join(category.split(' '))
        self.count = 0
        
    def updateScope(self,scope):
        if(self.count):
            self.scope['result'][start_url]+=scope['result'][start_url]
        else:
            self.scope=scope
        self.count += 1
        
    def saveScript(self,script):
        script_name = 'result/'+self.cate_str+'_attack'+str(self.count)+'.sh'
        with open(script_name, 'w') as f:
            f.write(script)

    def saveScope(self):
        file_name = 'result/'+self.cate_str+'_scope.json'
        with open(file_name,'w+') as f:
            json.dump(self.scope,f)

