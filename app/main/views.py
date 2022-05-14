from flask import render_template
from . import main
from ..requests import get_Quote

@main.route('/')
def index():

    quote = get_Quote()

    title = 'JAYMMY-TECH'
    return render_template('index.html', title = title, quote = quote)