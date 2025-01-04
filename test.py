import requests
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
from scraper import COUNTRY_CONFIG

app = Flask(__name__)

def fetch_headlines(country_code, site_name):
    # Check if the country and site exist in the config
    if country_code not in COUNTRY_CONFIG:
        raise ValueError(f"Country '{country_code}' not supported.")
    if site_name not in COUNTRY_CONFIG[country_code]:
        raise ValueError(f"Site '{site_name}' not found for country '{country_code}'.")

    # Get the site configuration
    site_config = COUNTRY_CONFIG[country_code][site_name]
    # Send the request and parse the content
    response = requests.get(site_config['url'])

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {site_config['url']}. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find headlines based on the tag and class
    headline_tag = site_config['headline_tag']
    headline_class = site_config['headline_class']
    
    # If class is specified, use it, else just use the tag
    if headline_class:
        headlines = soup.find_all(headline_tag, class_=headline_class)
    else:
        headlines = soup.find_all(headline_tag)
    
    # Extract and return the text from each headline
    return [headline.get_text() for headline in headlines]

@app.route("/")
def homepage():
    """ Serve the main page """
    return render_template("index.html")

@app.route("/get_news/<country_code>")
def get_news(country_code):
    """ Fetch and return news for the given country code. """
    try:
        headlines = []
        # Fetch news from all available sources for the country
        for site in COUNTRY_CONFIG.get(country_code, {}):
            site_headlines = fetch_headlines(country_code, site)
            headlines.extend(site_headlines)

        return jsonify({"headlines": headlines})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5002)