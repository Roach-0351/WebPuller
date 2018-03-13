import urllib.request
import urllib.error
import urllib.parse
import urllib.response
import re
from html.parser import HTMLParser
import os.path
import difflib
# from difflib_data import *
import _markupbase
import http
import rumps

# TODO need to add rumps package for system tray application
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
        self.site = self.page.read().decode('utf-8')
        self.sites = self.page.readlines()

        # self.site.decode("utf-8")

    def get_title(self):
        title = re.search('<title>(.*?)</title>', self.site)
        return title.group(1) + '.txt'

    def get_page(self):
        webpage_title = web.get_title()
        # print(self.site.decode("utf-8"))
        if os.path.exists(webpage_title) is False:
            # TODO should be writing one line to file, .txt extension possibly not necessary
            wepage_txt = open(webpage_title, 'w')
            wepage_txt.write(self.site)
        else:
            compared_files = web.compare_html(webpage_title)
    def compare_html(self, webpage_title):
        old_page = open(webpage_title, 'r')
        old_read = old_page.read()
        if old_read != self.site:
            print('files are different')
            print('old read contains -----------------------------------------------\n' + str(old_read))
            print('______________________________________________________________________________________________')
            print('current read contains ___________________________________________________________\n' + str(self.site))
#         TODO need to compare existing file with current read

    def strip_show(self):
        html = self.site.decode('utf-8')
        stripped_html = strip_tags(html)
        filtered = filter(lambda x: not re.match(r'^\s*$', x), stripped_html)
        pass
        # for line in stripped_html:
        #     if line is "" or line is '\n':
        #         continue


def strip_tags(html):
    s = MyParser()
    s.feed(html)
    return s.get_data()



if __name__ == '__main__':

    # webpage = input('Enter the name of the website you want to scrape for changes')
    webpage = 'http://rowdysites.msudenver.edu/~emersonb/Spring18/LinearAlgebraSp18.html'
    web = WebPuller()

    web.get_page()




