import requests
from utility import start_url, get_success_message

print '\n'
print 'start hidden resource'

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
        print get_success_message(url + '\t' + code)

print 'finish hidden resource'




