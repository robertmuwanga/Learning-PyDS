import requests
import os
import wget
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url) :
        self.url = url
        self.rss = None
        self.podcasts = None

    def download(self, downloadList):
        number_of_podcasts = len(downloadList)

        for i, podcast in enumerate(downloadList):
            if(os.path.exists(podcast.split('/')[-1])) :
                print('\n## Skipping {} of {}. File exists.'.format(i+1, number_of_podcasts))
            else:
                print('\n## Downloading {} of {}'.format(i+1, number_of_podcasts))
                wget.download(podcast)
                print('## Done. Downloaded {} of {}'.format(i+1, number_of_podcasts))

    def scrape(self) :
        self.rss = BeautifulSoup(requests.get(url).text, features='lxml')
        self.podcasts = [x['url'] for x in self.rss.find_all(name='enclosure')]
        
        return self.podcasts

if __name__ == '__main__':
    url = 'http://feeds.codenewbie.org/cnpodcast.xml'
    codenewbie = Scrape(url)
    
    print('\nDownloading CodeNewbie podcasts into current folder ....')
    codenewbie.download(codenewbie.scrape())

    print('\nDone scraping and downloading CodeNewbie podcasts.')