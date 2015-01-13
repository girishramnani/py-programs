import urllib.request
import urllib


import bs4
import shelve
work = shelve.open("last")

file = open("girish.html",'a')
def _check_the_last():
    t = work.get("first")
    while True:
        resp = urllib.request.urlopen('http://it-ebooks.info/book/{}/'.format(t))
        html = resp.geturl()

        if r"/404/" in html:
            work['last']=t
            break
        t+=1


def start_scrapping():
    _check_the_last()
    first=work.get("first")
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
                    final ='<a href="{}"> {} </a>'.format(t[2:-2],link.contents[0])
                    print("{} done..".format(x))
                    file.write(final)
                    file.write("<pre> ISBN : {}</pre>".format(link2.contents[0]))
                    file.write('<button style="display : inline;" onclick="location.href=\'http://it-ebooks.info/book/{}/\'" > book link </button>'.format(x))
                    file.write("<hr>" )


    except KeyboardInterrupt as e:
        print("done writing")
        file.close()
    work['first']=last


start_scrapping()