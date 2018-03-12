import urllib.request
import urllib.error
import urllib.parse
import urllib.response
import re
from html.parser import HTMLParser
import os.path
import _markupbase
import http
import rumps


class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        # self.strict = False
        # self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


class WebPuller:

    def __init__(self):
        self.page = urllib.request.urlopen(webpage)
        self.site = self.page.read()
        self.sites = self.page.readlines()

        # self.site.decode("utf-8")

    def get_title(self):
        title = re.search('<title>(.*?)</title>', self.site.decode("utf-8"))
        return title.group(1)

    def get_page(self):
        webpage_title = web.get_title()
        # print(self.site.decode("utf-8"))
        html = self.site.decode('utf-8')
        stripped_html = strip_tags(html)
        if os.path.exists(webpage_title + '.txt') is False:
            wepage_txt = open(webpage_title + '.txt', 'w')
            wepage_txt.write(stripped_html)
        else:
            print('File already exists')

def strip_tags(html):
    s = MyParser()
    s.feed(html)
    return s.get_data()



if __name__ == '__main__':

    # webpage = input('Enter the name of the website you want to scrape for changes')
    webpage = 'http://rowdysites.msudenver.edu/~emersonb/Spring18/LinearAlgebraSp18.html'
    web = WebPuller()

    web.get_page()




