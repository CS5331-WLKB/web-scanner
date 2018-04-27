import requests
from utility import *
# username and password from 8083
# look post_it_note
banner('Terminal Log In')

baseURL = 'http://ec2-52-77-212-149.ap-southeast-1.compute.amazonaws.com:8082'
username = 'tomhanks'
password = 'krakozia'

loginURL = baseURL + '/login/' + username + '/' + password
req = requests.get(loginURL)

success_message('username: ' + username + '\t' + 'pasword: ' + password)
