import urllib.request, json

def get_Quote():

    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = json.loads(url.read())