import requests
from utility import read_result, get_url, get_params, generate_url_with_params, get_success_message, OR

print '\n'
print 'start open redirect '

result = read_result()
links = result['link']

for link in links:
    url = get_url(link)
    params = get_params(url)
    params['redirect'] = 'https://www.google.com'
    fullURL = generate_url_with_params(url, params)
    req = requests.get(fullURL)
    if req.content.find('google') != -1:
        print get_success_message(fullURL)

print 'finish open redirect'
