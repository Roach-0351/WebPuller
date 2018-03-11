import urllib.request, urllib.error, urllib.parse, urllib.response, http, re
import rumps


class WebPuller:

    def __init__(self):
        self.page = urllib.request.urlopen(webpage)
        self.site = self.page.read()
        self.sites = self.page.readlines()
        # self.site.decode("utf-8")

    def get_title(self):
        title = re.search('<title>(.*?)</title>', self.site.decode("utf-8"))
        print(title)
        return title.group(1)

    def get_page(self):
        page_title = web.get_title()
        title_file = open(page_title + '.txt', 'w')


if __name__ == '__main__':

    # webpage = input('Enter the name of the website you want to scrape for changes')
    webpage = 'http://rowdysites.msudenver.edu/~emersonb/Spring18/LinearAlgebraSp18.html'
    web = WebPuller()
    web.get_page()




