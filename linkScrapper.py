from urllib.error import URLError
import urllib.request
import urllib


import bs4
import shelve
import os
work = shelve.open("last")

def _check_the_last():
    try:
        t = work.get('first')
    except Exception as E:
        t=1
    while True:
        resp = urllib.request.urlopen('http://it-ebooks.info/book/{}/'.format(t))
        html = resp.geturl()
        if r"/404/" in html:
            work['last']=t
            break
        t+=1


def start_scrapping():
    
    first=4716
    last = work.get('last')
    print(first,last)
    try:
        for x in range(first,last):
            response = urllib.request.urlopen('http://it-ebooks.info/book/{}/'.format(x))
            html = response.read()
            soup = bs4.BeautifulSoup(str(html)[2:-1])
            link2 = soup.find('b',itemprop='isbn')

            for link in soup.find_all('a'):
                t =str(link.get("href"))
                if "filepi" in t:
                    t2 = urllib.request.Request(t[2:-2],None,{"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0", "Referer":'http://it-ebooks.info/book/{}/'.format(x), "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
                    file_name =link.contents[0]
                    t2 = urllib.request.urlopen(t2)
                    url =t2.geturl()
                    count =0
                    while count<10:
                        print("starting .."+str(count))
                        erro_code= os.system("http {} --download -o \"{}\" --continue".format(url,file_name+".pdf"))
                        if erro_code ==0:
                            break
                        count+=1
                    else:
                        print("{} done..".format(x))
                    if count>=10:
                        pass


        work['first'] =work.get('last')


    except (URLError,ConnectionError,KeyboardInterrupt) as e:
        print("done writing")

        work['first']=x

        work.sync()


start_scrapping()
