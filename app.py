pip install Flask

from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)
url_mapping = {}

# Helper function to generate a short URL code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Home page to enter long URLs and get short URLs
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_mapping[short_code] = long_url
        return render_template('short_url.html', short_url=request.host_url + short_code)
    return render_template('index.html')

# Redirect short URLs to the original long URLs
@app.route('/<string:short_code>')
def redirect_to_long_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('error.html', message='URL not found')

if __name__ == '__main__':
    app.run(debug=True)
