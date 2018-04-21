import urllib, urllib2, os

DT = 'Directory Traversal'
SI = 'SQL Injection'
CSRF = 'CSRF'
OR = 'Open Redirect'
SSCI = 'Server Side Code Injection'
SCI = 'Shell Command Injection'

path = os.path.dirname(os.path.abspath(__file__))

def getHTML(url,params):
    data = urllib.urlencode(params)
    
    req = urllib2.Request(url,data)
    rsp = urllib2.urlopen(req)

    return rsp.read()
