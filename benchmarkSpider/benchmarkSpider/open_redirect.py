import requests
from utility import read_links, get_url, get_params, generate_url_with_params, get_success_message

print '\n'
print 'start open redirect '

for link in read_links():
    url = get_url(link)
    params = get_params(url)
    params['redirect'] = 'https://www.google.com'
    fullURL = generate_url_with_params(url, params)
    req = requests.get(fullURL)
    if req.content.find('google') != -1:
        print get_success_message(fullURL)

print 'finish open redirect'
