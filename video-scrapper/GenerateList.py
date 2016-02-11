from shelve import Shelf
import shelve

__author__ = 'Girish'

import requests
import bs4
t= shelve.open("links")

def __scrap():
    '''returns a list of links'''
    soup = bs4.BeautifulSoup(requests.get("http://pyvideo.org/category/").content)
    lis = soup.find_all("td")
    li=[]
    for x  in lis:
        if x.a != None:

            if not x.a.get("href").endswith("rss"):
                li.append(x.a.get("href"))
    return li
def terverse():
    global t

    if t:
        print("already done")

        return t['links']
    else:
        li = __scrap()
        t['links']=li
        return t['links']
def pop():
    print("removed")
    global t

    w = t['links']
    if w:
        temp= w.pop()
        t['links']=w
        t.sync()
        return temp

def peek():
    global t

    w = t['links']
    if w:
        temp= w.pop()
        return temp


