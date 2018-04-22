from utility import *
import json
'''
def saveScope(name,scope):
    with open(name, 'rb') as f:
        data = json.load(f,encoding='utf-8')
    if(data.keys()):
       data['result'][start_url]+=scope['result'][start_url]
       print data
    else:
        data = scope
    with open(name,'wb') as f:
        json.dump(data,f,encoding='utf-8')
'''        
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
    
    '''
    saveScope(scope_name,scope)
    with open(scope_name,'w+') as f:
        json.dump(scope,f)
    '''
    
    script = 'curl '+start_url+endpoint+'?'
    keys = params.keys()
    values = params.values()
    pair = [keys[i]+'='+values[i] for i in range(len(keys))]
    evil_param = '&'.join(pair)
    script+=evil_param
    script_name = path+'/result/DT_script.sh'
    '''
    with open(script_name,'w+') as f:
        f.write(script)
    ''' 
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
