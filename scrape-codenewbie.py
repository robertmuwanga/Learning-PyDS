import requests
import wget
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url) :
        self.url = urla

    def download(self, downloadList):
        for i, podcast in enumerate(downloadList):
            print('\n## Downloading {} of {}'.format(i+1, len(downloadList)))
            wget.download(podcast)

    def scrape(self) :
        codenewbie = BeautifulSoup(requests.get(url).text, features='lxml')
        podcasts = [x['url'] for x in codenewbie.find_all(name='enclosure')]
        
        return podcasts

if __name__ == '__main__':
    url = 'http://feeds.codenewbie.org/cnpodcast.xml'
    codenewbie = Scrape(url)
    codenewbie.download(codenewbie.scrape()[:2])

    print('\nDone scraping and downloading CodeNewbie podcasts.')