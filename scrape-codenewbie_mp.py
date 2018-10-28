import multiprocessing
import requests
import wget
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, url, n_processes = multiprocessing.cpu_count()) :
        self.url = url
        self.n_processes = n_processes

    def download(self, downloadList):
        pool = multiprocessing.Pool(self.n_processes)
        pool.map(wget.download, downloadList)
        pool.close()
        pool.join()

    def scrape(self) :
        codenewbie = BeautifulSoup(requests.get(url).text, features='lxml')
        podcasts = [x['url'] for x in codenewbie.find_all(name='enclosure')]
        
        return podcasts

if __name__ == '__main__':
    url = 'http://feeds.codenewbie.org/cnpodcast.xml'
    codenewbie = Scrape(url)
    codenewbie.download(codenewbie.scrape()[:2])

    print('\nDone scraping and downloading CodeNewbie podcasts.')