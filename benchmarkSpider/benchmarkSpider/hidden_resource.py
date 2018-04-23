import requests
from utility import *

banner(HR)

commons = 'hidden_resource_commons.txt'
f = open(commons, 'r')
injections = f.read().splitlines()

for injection in injections:
    url = start_url + '/' + injection
    req = requests.get(url)
    code = str(req.status_code)

    # retrieve the redirect status code
    if req.history != []:
        first = req.history[0]
        code = str(first.status_code)

    if '200' <= code < '300':
        success_message(url + '\t' + code)

print '\n'
