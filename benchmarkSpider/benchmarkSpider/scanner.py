class Scanner(object):
    def __init__(self,url):
        self.url = url
        self.vul_info = {}
        self.attack_script = ''
        self.safe = True

    def scan(self):
        if (
            sqli() or
            serverInj() or
            dirTra() or
            redir() or
            csrf() or
            shellInj()
        ):
            self.safe = False
    
    def dirTra(self):
        category = "Directory Traversal"
        
        return False        

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
        
    def genInfo(self):
        pass
    
    

    
        
