from urllib.error import URLError
import urllib.request
import urllib


import bs4
import shelve
import os
work = shelve.open("last")

def start_scrapping():
    import sys
    import itertools

    first=work.get('first')
    print(work['first'])
    print(sys.argv)


    if len(sys.argv) ==3:
    	first = int(sys.argv[1])
    	last = int(sys.argv[2])
    elif len(sys.argv) ==2:
    	first = int(sys.argv[1])

    try:
        tried_next = False
        for number in itertools.count(first):
            print("Downloading {}".format(number))
            response = urllib.request.urlopen('http://it-ebooks.info/book/{}/'.format(number))
            html_url = response.geturl()
            if r"/404/" in html_url:
                if tried_next == True:
                    work['last']=number
                    print("Done with download")
                    break
                tried_next = True
                continue

            html = response.read()
            soup = bs4.BeautifulSoup(str(html)[2:-1])

            for link in soup.find_all('a'):
                t =str(link.get("href"))
                if "filepi" in t:
                    t2 = urllib.request.Request(t[2:-2],None,{"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0", "Referer":'http://it-ebooks.info/book/{}/'.format(number), "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
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
                        print("{} done..".format(number))
                    if count>=10:
                        pass
            tried_next = False


        work['first'] =work.get('last')


    except (URLError,ConnectionError,KeyboardInterrupt) as e:
        print(e)

        work['first']=number

        work.sync()

start_scrapping()
