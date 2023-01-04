"""
----------------------------
Web-scraping dev.to articles
----------------------------
"""

from sys import argv
import requests
from const import *
from article import Article
from bs4 import BeautifulSoup

def get_args() -> tuple:
    topic = argv[1] if len(argv) >= 2 else DEF_TOPIC
    limit = int(argv[2]) if len(argv) >= 3 else DEF_LIMIT
    return (topic, limit)

def scrape_articles(html_soup: BeautifulSoup, limit: int) -> list:
    elements = html_soup.find_all("div", {"class": ARTICLE_CN }, limit=limit)
    for el in elements:
        title_el = el.find("h2", {"class": TITLE_CN})
        title = title_el.text.strip()
        link = DEVTO_URL + title_el.find("a", href=True)["href"]
        author = el.find("a", {"class": AUTHOR_CN}).text.strip()
        date = el.find("a", {"class": DATE_CN}).text
        yield Article(title, link, author, date)

topic, limit = get_args()
SCRAPE_URL=f"{DEVTO_URL}/t/{topic}"
r = requests.get(SCRAPE_URL) # get a response from the website
soup = BeautifulSoup(r.text, "html.parser")
articles = scrape_articles(soup, limit)

print(f'\n{"-" * 31} {topic.capitalize()} articles {"-" * 31}')
for article in articles:
    print(article)