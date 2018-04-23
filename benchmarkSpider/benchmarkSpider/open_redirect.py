import requests
from generator import render, generator
from utility import *

banner(OR)
links = read_links()
results = read_result()
redirect_url = 'https://www.google.com'


OR_generator = generator(OR)

for link in links:
    url = get_url(link)
    params = get_params(url)
    if params:
	get_method = 'GET'
	for param in params:
	    temp_params = params.copy()
            temp_params[param] = redirect_url
    	    fullURL = generate_url_with_params(url, temp_params)
            req = requests.get(fullURL)
            if req.history:
	        endpoint = url.path
                scope, script = render[OR](endpoint,temp_params,get_method)
                OR_generator.updateScope(scope)
                OR_generator.saveScript(script)                        
                success_message(fullURL)

for obj in results:
    post_method = 'POST'
    link = obj['link']
    input_names = obj['content']
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
            	scope,script = render[OR](endpoint,params,input_names)
            	OR_generator.updateScope(scope)
            	OR_generator.saveScript(script)
            	success_message(link + '\t' + json.dumps(payload))

OR_generator.saveScope()

print '\n'
