import urllib.request, json
from app.models import Quote

def get_Quote():

    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = json.loads(url.read())

        get_quote_results = None

        if get_quote_data:
            author = get_quote_data['author']
            id = get_quote_data['id']
            quote = get_quote_data['quote']
            permalink = get_quote_data['permalink']

            get_quote_results = Quote(author, id, quote, permalink)

    return get_quote_results