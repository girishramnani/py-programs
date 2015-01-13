__author__ = 'girish'


import urllib.request
w =urllib.request.urlopen(r"http://pyvideo.org/video/rss")
html = w.read()

print(html)