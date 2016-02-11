'''requirements requests , bs4'''
import shelve

__author__ = 'girish'
import requests
from bs4 import BeautifulSoup as Soup
import GenerateList as Gl
import os


import os

def fetch_youtube_urls(category_url):
    # Scrape the pyvideo site to get titles and descriptions of
    # each video so you can choose which you want to download.
    url=[]
    j =0
    soup = Soup(requests.get(category_url).content)

    for div in soup.find_all('a', attrs={'class': 'thumbnail'}):
        video_path = div['href']
        video_url = 'http://pyvideo.org{}'.format(video_path)
        video_soup = Soup(requests.get(video_url).content)
        print("parsing the link .. \n {}".format(video_path))
        yield video_soup.find('div',attrs={'class':'amara-embed'})['data-url']


def download_video(url):
    # Use youtube-dl to handle the download
    os.system('youtube-dl "%s"' % url)


def notify(msg):
    line = '-' * len(msg)
    print ("\n%s\n%s\n%s\n\n" % (line, msg, line))

if __name__ == '__main__':


    '''change the link to download appropriate event videos'''
    pyvid_url = 'http://pyvideo.org/category/17/pycon-us-2012'

    notify('Fetching video URLs from %s' % pyvid_url)
    for url in fetch_youtube_urls(pyvid_url):
        notify('Downloading %s' % url)
        flv_filename = download_video(url)

        notify('Video fetching complete')
