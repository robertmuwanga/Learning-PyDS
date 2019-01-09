# Let's get the necessary libraries
import pandas as pd
import requests
import os
import wget
from bs4 import BeautifulSoup

# Set the URL for the RSS feed
url = 'http://feeds.harvardbusiness.org/harvardbusiness/ideacast'

# List podcast episodes of interest. Put 'None' for all.
podcasts = ['660', '659', '651', '648', '647', '642', '640', '630', '628', '625', '616',  
            '654', '653', '652', '650', '649', '645', '644', '639', '638', '637', '629',  
                '627', '626', '623', '622', '621', '620', '617', '615', '612', '611', '610', 
            '658', '657', '646', '634', '633', '631', '624', '619', '614', '613', '608'
]

# Scape podcast listing from podcast list
rss = BeautifulSoup(requests.get(url).text, features='lxml')

titles = [title.string for title in (rss.find_all('title'))][2:] # the first two are irrelevant
descriptions = [description.string for description in (rss.find_all('description'))][1:] # the first is irrelevant
links = [link['url'] for link in (rss.find_all('enclosure'))]

indices_with_podcasts = []
podcast_dict = {}

if podcasts == None:
    raise NotImplementedError() # To be implemented in due time

for podcast in podcasts : 
    for index, item in enumerate(titles) :
        if podcast in item:
            indices_with_podcasts.append((index, podcast))

for item in indices_with_podcasts:
    podcast_dict[item[1]] = {'title' : titles[item[0]], 'description' : descriptions[item[0]], 'link' : links[item[0]]}

df = pd.DataFrame.from_dict(podcast_dict, orient='index')

print('Downloading audio files:')

for link in df['link'] : 
    wget.download(link)

print('Done downloading audio files.')

print('Writing to Excel file.')
df.to_excel('HBR.xlsx')

print('Completed Script.')

