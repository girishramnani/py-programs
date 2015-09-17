from concurrent.futures.thread import ThreadPoolExecutor

__author__ = 'Girish'


import requests
from queue import Queue
import bs4
import shelve

data = shelve.open("remember",writeback=True)


try:
    starting = data["last"]
except:
    starting =1
html_pages = []


for i in range(starting):
    response = requests.get("http://finance.yahoo.com/mb/forumview/?&v=m&bn=072b030b-a126-32f4-b237-4f342be9ed44&page={}".format(i))
    html_pages.append(response.content.decode())



