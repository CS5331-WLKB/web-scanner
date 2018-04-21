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
        
    def scan(self):
        if (
            self.sqli() or
            self.serverInj() or
            self.dirTra() or
            self.redir() or
            self.csrf() or
            self.shellInj()
        ):
            self.safe = False
        if self.safe:
            print(self.category)
    
    def dirTra(self, depth=10):
        feed = ["etc/passwd"]
        prefix = '../'
        url_parsed = urlparse(self.url)
        params = url_parsed.params
        nuggets = ['root/:/bin/bash']
        key_params = {}
        print(params)
        
        i = 0
        hit = False
        
        if(not params): # if url contain no parameters
            return False
        else:
            for p in parms:
                if hit: # if already hit
                    break
                # brute exploite by incremently adding '../'
                while i < depth and not hit :
                    # exploite every paramters in the url
                    for f in feed:
                        evil_param = i*prefix+f
                        content = str(getHTML(self.base,{f:evil_para}))
                        for n in nuggets:
                            if n in content:
                                hit = True
                                key_params = evil_param
                i+=1

        if hit:
            self.category = DT
            endpoint = '/'+self.base.split('/')[:-1]
            render[DT](self.base,endpoint,key_params,'GET')
        return hit
                    

    def serverInj(self):
        category = "Shell Injection"
        return False
    
    def shellInj(self):
        return False

    def redir(self):
        return False

    def sqli(self):
        return False

    def csrf(self):
        return False
        
    

    
        
