import urllib.request
from bs4 import BeautifulSoup
import os


class Scraper:
    #
    path = os.path.join("/home", "dmitriy", "learning_python", "url.html")
    n = 1

    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        url_file = open(self.path, "w")
        for tag in sp.find_all(class_="DY5T1d"):
            url_str = str(tag)
            if url_str is None:
                continue
            url_file.write("<p> {}) - ".format(self.n) + url_str + "</p>")
            self.n += 1
        url_file.write('\n<base href="https://news.google.com/"</>')
        url_file.close()


news = "https://news.google.ru/"
Scraper(news).scrape()
