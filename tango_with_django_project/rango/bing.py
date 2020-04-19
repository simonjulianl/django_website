import json
import urllib
import urllib.request as request
import requests

def read_bing_key():
    bing_api_key = None
    try :
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except :
        raise IOError('not found ! ')

    return bing_api_key

def run_query(search_terms):
    """
    given the query return the list of results
    """

    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError("Bing Key Not Found !")

    root_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    service = ""

    results_per_page = 10
    offset = 0

    query = "'{}'".format(search_terms)
    query = urllib.parse.quote(query)

##    search_url = "{}{}?$format=json&$tp={}&$skip={}&Query={}".format(
##        root_url,
##        service,
##        results_per_page,
##        offset,
##        query)


    payload = {'q' : search_terms,
               'tp' : results_per_page,
               'skip' : offset}
    headers = {'Ocp-Apim-Subscription-Key':bing_api_key}
    r = requests.get(root_url, params = payload, headers = headers)

    result = r.json()
    result = result.get('webPages', {}).get('value',{})
    
    results = []
    
    for key in result:
        results.append({'title' : key.get('name','not found'),
                        'link' : key.get('url','not found'),
                        'snippet' : key.get('snippet','not found')})
    return results
    

##    username = ''
##    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
##    password_mgr.add_password(None, search_url, username, bing_api_key)
##    #the sequence is realm, url , user, password
##
##    results = []


##    try :
##        handler = request.HTTPBasicAuthHandler(password_mgr)
##        opener = request.build_opener(handler)
##        request.install_opener(opener)
##        response = urllib.request.urlopen(search_url).read()
##        response = response.decode('utf-8')
##
##        json_response = json.loads(response)
##
##        for result in json_response['d']['results']:
##            results.append({'title':result['Title'],
##                            'link':results['Url'],
##                            'summary' : result['Description']})
##
##    except :
##        print('Error in query')

if __name__ == "__main__":
    query = input('query : ')
    
