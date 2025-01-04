import requests
from bs4 import BeautifulSoup

#to print headlines and headline count (modify accordingly)
#headlines = fetch_USA_cnn()
    #print(f"Found {len(headlines)} headlines")
    #for headline in headlines:
        #print(headline)
### MAYBE CREATE 3 TABS UNDER EACH PANEL for each site

#, class_='c-article__title'

response = requests.get('https://elperiodic.ad/')
soup = BeautifulSoup(response.content, 'html.parser')
headlines = soup.find_all('h5')
headlines = [headline.get_text() for headline in headlines]
print(f"Found {len(headlines)} headlines")
for headline in headlines:
    print(headline,"\n")
        

COUNTRY_CONFIG = {
    "AD": {#Andorra
        "bondia": {
            "url": "https://www.bondia.ad/totes-les-noticies",
            "headline_tag": "a",
            "headline_class": {"font-bold pt-2"}
        },
        "elperiodic": {
            "url": "https://elperiodic.ad/",
            "headline_tag": "h5",
            "headline_class": {"elementor-heading-title elementor-size-default"}
        },
        "diari": {
            "url": "https://www.diariandorra.ad/nacional/",
            "headline_tag": "h2",
            "headline_class": {"c-article__title"}
        }
    },
    "AE": {#United Arab Emirates
        "khaleej": {
            "url": "https://www.khaleejtimes.com/uae-latest-news",
            "headline_tag": "h2",
            "headline_class": {"post-title"}
        },
        "gulf": {
            "url": "https://gulfnews.com/uae",
            "headline_tag": "h2",
            "headline_class": {"card-title"}
        },
        "national": {
            "url": "https://www.thenationalnews.com/news/uae/",
            "headline_tag": "p",
            "headline_class": {"defaultstyled__StyledHeadline-sc-1dedoj7-8 dyVOMW b-pmed order-0"}
        }
    },
    "AF": {#Afghanistan
        "khaama": {
            "url": "https://www.khaama.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        },
        "pajhwok": {
            "url": "https://pajhwok.com/",
            "headline_tag": "h4",
            "headline_class": {"d-none d-sm-block story-title mt-1"}
        },
        "bakhtar1": {
            "url": "https://www.bakhtarnews.af/en/category/news/",
            "headline_tag": "li",
            "headline_class": {"news-item"}
        },
        "bakhtar2": {
            "url": "https://www.bakhtarnews.af/en/category/news/page/2/",
            "headline_tag": "li",
            "headline_class": {"news-item"}
        }
    },
    "AG": {#Antigua and Barbuda
        "newsroom": {
            "url": "https://antiguanewsroom.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        },
        "herald": {
            "url": "https://antiguanherald.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        }
    },
    "AI": {#Anguilla!!!!!!!!!!!!!!
        "newsroom": {
            "url": "https://antiguanewsroom.com/",
            "headline_tag": "h3",
            "headline_class": None
        },
        "herald": {
            "url": "https://antiguanherald.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        },
        "tvradio": {
            "url": "https://abstvradio.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        }
    },
    "AL": {#Albania !!!!!!!!!!!!
        "newsroom": {
            "url": "https://antiguanewsroom.com/",
            "headline_tag": "h3",
            "headline_class": None
        },
        "herald": {
            "url": "https://antiguanherald.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        },
        "tvradio": {
            "url": "https://abstvradio.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        }
    },
    "AM": {#Armenia !!!!!!!!!!!!!!!!!!!
        "newsroom": {
            "url": "https://antiguanewsroom.com/",
            "headline_tag": "h3",
            "headline_class": {""}
        },
        "herald": {
            "url": "https://antiguanherald.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        },
        "tvradio": {
            "url": "https://abstvradio.com/",
            "headline_tag": "h3",
            "headline_class": {"entry-title td-module-title"}
        }
    },
    "GB": {#United Kingdom
        "bbc": {
            "url": "https://www.bbc.com/news/uk",
            "headline_tag": "h2",
            "headline_class": {"data-testid": "card-headline"}
        },
        "guardian": {
            "url": "https://www.theguardian.com/uk-news",
            "headline_tag": "span",
            "headline_class": {"show-underline dcr-uyefka"}
        }
    },
    "US": {#United States
        "cnn": {
            "url": "https://www.cnn.com/",
            "headline_tag": "span",
            "headline_class": {"class": "container__headline-text"}
        },
        "fox": {
            "url": "https://www.foxnews.com/",
            "headline_tag": "h3",
            "headline_class": {"title"}
        },
        "nyt": {
            "url": "https://www.nytimes.com/",
            "headline_tag": "p",
            "headline_class": {"class": "indicate-hover"}
        }
    }
}