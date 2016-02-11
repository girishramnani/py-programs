import shelve

__author__ = 'Girish'
import bs4 as Soup
import requests
import GenerateList as Gl
Gl.terverse()

def fetch_youtube_urls(category_url):
    # Scrape the pyvideo site to get titles and descriptions of
    # each video so you can choose which you want to download.
    url=[]
    j =0
    soup = Soup.BeautifulSoup(requests.get(category_url).content)

    for div in soup.find_all('a', attrs={'class': 'thumbnail'}):
        video_path = div['href']
        video_url = 'http://pyvideo.org{}'.format(video_path)
        video_soup = Soup.BeautifulSoup(requests.get(video_url).content)
        print("parsing the link .. \n {}".format(video_path))
        yield video_soup.find('div',attrs={'class':'amara-embed'})['data-url']

while Gl.peek() != None:
    con = Gl.peek()
    t2 = con.split("/")[-1]
    file = open("girish\\"+t2+".txt","w+")
    print("at {}".format(t2))
    pv_location = "http://pyvideo.org"+con
    for x in fetch_youtube_urls(pv_location):
        file.write(x+"\n")
    file.flush()
    file.close()
    Gl.pop()




