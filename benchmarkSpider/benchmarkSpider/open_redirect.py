import requests
from utility import *

banner(OR)

for link in read_links():
    url = get_url(link)
    params = get_params(url)
    params['redirect'] = 'https://www.google.com'
    fullURL = generate_url_with_params(url, params)
    req = requests.get(fullURL)
    if req.content.find('google') != -1:
        success_message(fullURL)

print '\n'
