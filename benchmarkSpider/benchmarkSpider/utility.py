import urllib
import urllib2
import os
import json
import urlparse
from termcolor import colored

domain = 'target.com'
start_url = 'http://target.com'

HR = 'Hidden Resource'
DT = 'Directory Traversal'
SI = 'SQL Injection'
CSRF = 'CSRF'
OR = 'Open Redirect'
SSCI = 'Server Side Code Injection'
SCI = 'Shell Command Injection'
HP = 'Hack Password'

path = os.path.dirname(os.path.abspath(__file__))
resultpath = os.path.join(path, 'result/result.json')


def read_results():
    results = []
    try:
        with open(resultpath,'r') as f:
            try: 
                for line in f.readlines():
                    result = json.loads(line)
                    results.append(result)
                return results
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


def success_message(message):
    print "\n\t[+] Detection results:"
    print "\t------------------"
    print "\t" + colored('Success! ', 'green') + message


def banner(title):
    print "\n***************************************"
    print "* " + title + "                       *"
    print "***************************************"
