import requests
from queue import Queue
import bs4
import shelve
from scrapper import find_next,get_scrap_data

data = shelve.open("remember",writeback=True)


try:
    starting = data["last"]
except:
    starting =1
html_pages = []

for i in range(starting):
    response = requests.get("http://finance.yahoo.com/mb/forumview/?&v=m&bn=072b030b-a126-32f4-b237-4f342be9ed44&page={}".format(i))
    html_pages.append(response.content.decode())


get_scrap_data(html_pages)


