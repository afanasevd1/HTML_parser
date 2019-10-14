import urllib.request
from bs4 import BeautifulSoup
import os


class Scraper:

    os_path = os.getenv("HOME")
    path = os.path.join(os_path + "/url.html")
    news_num = 1

    def __init__(self, site):
        self.site = site

    def scrape(self):
        html = urllib.request.urlopen(self.site).read()
        parser = "html.parser"
        with open(self.path, "w") as url_file:
            for tag in BeautifulSoup(html, parser).find_all(class_="DY5T1d"):
                url_str = str(tag)
                if url_str is None:
                    continue
                url_file.write("<p> {}) - ".format(self.news_num) + url_str + "</p>")
                self.news_num += 1
            url_file.write('\n<base href="https://news.google.ru/"</>')


news = "https://news.google.ru/"
Scraper(news).scrape()
