import requests

import json
from utility import *
from generator import generator, render

banner(SI)

result = read_result()
links = result['link']
commons = 'sql_injection_commons.txt'
f = open(commons, 'r')
injections = f.read().splitlines()

SI_geneartor = generator(SI)

for link in links:
    for injection in injections:
        payload = {
            'username': injection
        }
        req = requests.post(link, data=payload)
        if req.content.find('We found you') != -1:
            success_message(link + '\t' + json.dumps(payload))

print '\n'
