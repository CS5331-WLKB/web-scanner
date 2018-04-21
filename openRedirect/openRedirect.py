import json
import urllib,urllib2,cookielib,webbrowser
import urlparse


file = open('../benchmarkSpider/benchmarkSpider/result.json','r')
for line in file.readlines():
    dict = json.loads(line)
    #print(dict['link'])
    link = str(dict['link'])
    #print("redirect:",link)
    url = urlparse.urlparse(link)
    origin_params = urlparse.parse_qs(url.query)
    if origin_params:
        print origin_params
        for param in origin_params:
	    params = origin_params.copy()
	    params[param]='http://www.google.com'
	    full_url = url._replace(query = urllib.urlencode(params,True)).geturl()
	    print(full_url)
	    #webbrowser.open(full_url,new=2)
	    
		
    	
