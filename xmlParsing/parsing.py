__author__ = 'Girish'
import xml.sax as x
import time
import requests
class ConHandler(x.ContentHandler):
    def __init__(self):
        x.ContentHandler.__init__(self)
    def startElement(self, name, attrs):
        if name =="component":
            print(attrs.getValue("name"))

x.parse(open("misc.xml"),ConHandler())
print()


