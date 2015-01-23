__author__ = 'Girish'
import xml.sax as parser

class ConHandler(parser.ContentHandler):
    def __init__(self):
        parser.ContentHandler.__init__(self)
    def startElement(self, name, attrs):
        if name =="component":
            print(attrs.getValue("name"))

parser.parse(open("misc.xml"),ConHandler())
print()


