__author__ = 'Girish'
__author__ = 'Girish'

'''requirements requests , bs4'''
import shelve

__author__ = 'girish'
import requests
from bs4 import BeautifulSoup as Soup
import optparse
import os
import sys

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
        try:
            yield video_soup.find('div',attrs={'class':'amara-embed'})['data-url']
        except:
            continue

def download_video(url, foldername):
    # Use youtube-dl to handle the download
    return os.system('youtube-dl -o ".\\{}\\%(title)s.%(ext)s" "{}"'.format(foldername ,url))


def notify(msg):

    line = '-' * len(msg)
    print ("\n%s\n%s\n%s\n\n" % (line, msg, line))

def working():

    try:
        pick = shelve.open("downloaded2")

        if not pick:
            pick["down"]=set([])


        t= pick['down']


        if len(sys.argv) ==1:
            foldername = pick['folder']
            link = pick['link']
            print(foldername)
        else:
            foldername =sys.argv[1].split("/")[-1]
            link = sys.argv[1]
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        '''change the link to download appropriate event videos'''
        pyvid_url = 'http://pyvideo.org/category/'+link

        notify('Fetching video URLs from %s' % pyvid_url)
        for url in fetch_youtube_urls(pyvid_url):
            if not (url in pick['down']):
                notify('Downloading %s' % url)
                exit_code= download_video(url,foldername)
                print(exit_code)
                if int(exit_code)==0:
                    t.add(url)
                    pick['down']=t
                    pick.sync()
                else:
                    print("Error..")

            else:
                print("skipping {}".format(url))
        pick['down']=set([])

        notify('Video fetching complete')

    except KeyError:
        pick.sync()
        sys.exit(-1)

    except KeyboardInterrupt:

        pick['folder'] = foldername
        pick['link']= link
        pick.sync()
        print("Exiting")
        sys.exit()
count=0
try:
    count+=1
    working()
except ConnectionError:
    print("trying again..")
    if count <5:
        working()



