from requests.models import Response

__author__ = 'Girish'
import requests
from bs4 import BeautifulSoup as soup
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

URL ="https://cricket.yahoo.com/cricket/live-score/#live"

r = Render(URL)
result = r.frame.toHtml()
work = soup(result)
print(work.prettify())