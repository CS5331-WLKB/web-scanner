import urllib
import urllib2
import os
import json
import urlparse
from termcolor import colored

domain = 'target.com'
start_url = 'http://target.com'

DT = 'Directory Traversal'
SI = 'SQL Injection'
CSRF = 'CSRF'
OR = 'Open Redirect'
SSCI = 'Server Side Code Injection'
SCI = 'Shell Command Injection'

path = os.path.dirname(os.path.abspath(__file__))
resultpath = os.path.join(path, 'result.json')

def read_links():
    links = []
    try:
        with open(resultpath,'r') as f:
            try: 
                for line in f.readlines():
                    link = str(json.loads(line)['link'])
                    links.append(link)
                return links
            except ValueError:
                print 'fail to load url file'
    except IOError:
        print 'fail to open url json file'


def get_url(link):
    return urlparse.urlparse(link)


def get_params(url):
    return urlparse.parse_qs(url.query)


def generate_url_with_params(url, params):
    return url._replace(query=urllib.urlencode(params, True)).geturl()


def get_success_message(message):
    return colored('Success! ', 'green') + message
