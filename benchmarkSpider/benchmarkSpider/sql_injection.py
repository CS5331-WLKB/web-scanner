import requests
import json
from utility import *
from generator import generator, render

banner(SI)

method = 'POST'

results = read_result()

commons = 'sql_injection_commons.txt'
nugget = 'We found you!'

f = open(commons, 'r')
injections = f.read().splitlines()

SI_generator = generator(SI)

for obj in results:
    link = obj['link']
    input_names = obj['content']
    url = get_url(link)
    if len(input_names):
        for injection in injections:
            for p in input_names:
                payload = {
                    p: injection
                }
                req = requests.post(link, data=payload)
                if req.content.find(nugget) != -1:
                    endpoint = url.path
                    params = payload
                    scope,script = render[SI](endpoint,params,method)
                    SI_generator.updateScope(scope)
                    SI_generator.saveScript(script)
                    success_message(link + '\t' + json.dumps(payload))

SI_generator.saveScope()
print '\n'
