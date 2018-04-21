import urllib, urllib2, os

domain = 'target.com'
start_url = 'http://target.com'

DT = 'Directory Traversal'
SI = 'SQL Injection'
CSRF = 'CSRF'
OR = 'Open Redirect'
SSCI = 'Server Side Code Injection'
SCI = 'Shell Command Injection'

path = os.path.dirname(os.path.abspath(__file__))

def getHTML(url,params):
    data = urllib.urlencode(params)
    rsp = ''
    try:
        rsp = urllib2.urlopen(url+"?"+data)
    except urllib2.HTTPError:
        pass

    return rsp.read() if rsp else rsp

def getParams(url):
    result = {}
    url_split= url.split('?')
    if len(url_split) < 2: return result
     
    values = url_split[-1]
    for key in values.split('&'):
        pair = key.split('=')
        result[pair[0]]=pair[1]
    return result
