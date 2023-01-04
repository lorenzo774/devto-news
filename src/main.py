"""
Web-scraping dev.to react articles
"""
import requests
from const import *
from article import Article
from bs4 import BeautifulSoup

def scrape_articles(html_soup: BeautifulSoup, limit: int) -> list:
    elements = html_soup.find_all("div", {"class": ARTICLE_CN }, limit=limit)
    for el in elements:
        title_el = el.find("h2", {"class": TITLE_CN})
        title = title_el.text.strip()
        link = DEVTO_URL + title_el.find("a", href=True)["href"]
        author = el.find("a", {"class": AUTHOR_CN}).text.strip()
        date = el.find("a", {"class": DATE_CN}).text
        yield Article(title, link, author, date)

r = requests.get(SCRAPE_URL) # get a response from the website
soup = BeautifulSoup(r.text, "html.parser")
articles = scrape_articles(soup, LIMIT)

print(f'\n{"-" * 31} ⚛️ React articles {"-" * 31}')
for article in articles:
    print(article)