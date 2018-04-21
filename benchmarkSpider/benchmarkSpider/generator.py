from utility import *


def genDT(base,endpoint,params,method):
    scope = {
        'class':DT,
        'result':{
            base: [
                {
                    'endpoint': endpoint,
                    'params': params,
                    'method': 'GET'
                }
            ]
        }
    }

    scope_name = path + '/result/DT_scope.json'
    with open(scope_name,'w+') as f:
        json.dump(scope,f)


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
