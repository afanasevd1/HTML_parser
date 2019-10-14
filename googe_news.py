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
        url_file = open(self.path, "w")
        for tag in BeautifulSoup(html, parser).find_all(class_="DY5T1d"):
            url_str = str(tag)
            if url_str is None:
                continue
            url_file.write("<p> {}) - ".format(self.news_num) + url_str + "</p>")
            self.news_num += 1
        url_file.write('\n<base href="https://news.google.ru/"</>')
        url_file.close()


news = "https://news.google.ru/"
Scraper(news).scrape()
