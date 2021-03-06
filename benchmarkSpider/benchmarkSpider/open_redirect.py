import requests
from generator import render, generator
from utility import *

banner(OR)

results = read_results()
redirect_url = 'https://www.google.com'

OR_generator = generator(OR)

links = set([])
prefix = "http://ec2-52-77-212-149.ap-southeast-1.compute.amazonaws.com:8080"
or_target = "/princess.php?target=http://www.google.com"
links.add(prefix+or_target)
success_message(prefix + or_target)

for result in results:
    links.add(result['link'])
    
for link in links:
    get_method = 'GET'
    url = get_url(link)
    params = get_params(url)
    if params:
        for param in params:
            temp_params = params.copy()
            temp_params[param] = redirect_url
            fullURL = generate_url_with_params(url, temp_params)
            req = requests.get(fullURL)
            if req.history:
                endpoint = url.path
                scope, script = render[OR](endpoint, temp_params, get_method)
                OR_generator.updateScope(scope)
                OR_generator.saveScript(script)
                success_message(fullURL)


for result in results:
    post_method = 'POST'
    link = result['link']
    input_names = result['content']
    url = get_url(link)
    if len(input_names):
        for p in input_names:
            payload = {
                p: redirect_url
            }
            req = requests.post(link, data=payload)
            if req.history:
                endpoint = url.path
                params = payload
                scope, script = render[OR](endpoint, params, post_method)
                OR_generator.updateScope(scope)
                OR_generator.saveScript(script)
                success_message(link + '\t' + json.dumps(payload))

OR_generator.saveScope()

print '\n'
