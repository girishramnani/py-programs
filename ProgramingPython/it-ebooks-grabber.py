#!/usr/bin/python

# Title:    it-ebooks-grabber.py
# Author:   Daxda
# Date:     30.12.2013
# Desc:     Grabs the latest eBooks from it-ebooks.info

import urllib2, urllib, http.cookiejar as cookielib, http.cookies as Cookie, re,os, configparser as ConfigParser
from xml.dom.minidom import parseString
from time import sleep


class BookGrab():
    def __init__(self):
        self._loadConfig()

    def startGrabbing(self):
        """ Starts the grabbing loop """
        while 1:
            try:
                self._main()
                sleep(self._sleep)
            except KeyboardInterrupt:
                break
        return


    def _main(self):
        # connect to the site and extract the sites
        links = self._getBookLinks()
        for url in links:
            # check if we visited this url yet
            if url in self._visitedUrls:
                continue
            source = self._getSource(url)
            if not source:
                continue
            # extract the download link for the file and it's title
            downloadLink = self._getDlLink(source)
            bookTitle = self._getBookTitle(source)
            
            # download and save the file
            data = self._downloadFile(downloadLink, url)
            self._saveFile(bookTitle, data)

            # add the visited url to the list
            self._addToVUrls(url)

        return


    def _createConfig(self):
        """ Creates the config file for the grabber """
        with open("grab.conf", "w") as cfgfile:
            cfg = ConfigParser.ConfigParser()
            # start adding the parameters and its values
            cfg.add_section("Paths")
            cfg.set("Paths", "savePath", "ebooks/")
            cfg.set("Paths", "visitedUrls", "visited.txt")

            cfg.add_section("Connection")
            cfg.set("Connection", "sleep", "60")
            cfg.set("Connection", "userAgent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0")

            # write and close the file
            cfg.write(cfgfile)
        return


    def _cfgLoaded(self, valueName):
        """ Checks if all values have been loaded from the config file, returns bool """
        if not self._savePath:
            return False
        elif not self._visitedUrlsPath:
            return False
        elif not self._userAgent:
            return False
        elif not self._sleep:
            return False
        return True


    def _loadConfig(self):
        """ Loads the config file, if it doesn't exist it gets created """
        if os.path.isfile("grab.conf") is False:
            self._createConfig()
        
        try:
            # read the config and load its values
            c = ConfigParser.ConfigParser()
            c.read("grab.conf")
            self._savePath = c.get("Paths", "savePath")
            self._visitedUrlsPath = c.get("Paths", "visitedUrls")
            self._userAgent = c.get("Connection", "userAgent")
            tmpsleep = c.get("Connection", "sleep")
            try: # convert the sleep time to int
                if int(tmpsleep) < 30 or int(tmpsleep) > 1337:
                    self._sleep = 60
            except ValueError:
                self._sleep = 60
            else:
                self._sleep = int(tmpsleep)


            # add a trailing slash after the save path if required
            if self._savePath.endswith("/") is False:
                self._savePath += '/'

            try:
                # load the visited urls
                with open(self._visitedUrlsPath, "r") as f:
                    self._visitedUrls = [vurl.strip() for vurl in f.readlines()]
            except IOError:
                self._visitedUrls = []

            # make sure all values of the config were loaded
            if self._cfgLoaded is False:
                raise ValueError
        except(ConfigParser.NoOptionError, ValueError):
            print("Error: config file is missing crucial values!")
            exit(1)
        return


    def _getSource(self, url):
        """ Gets the source of the passed url """
        try:
            source = "" 
            u = urllib2.Request(url, None, {"User-Agent": self._userAgent})
            u = urllib2.urlopen(u)
            # filter out unsuccessful requests
            if u.code != 200:
                raise urllib2.HTTPError
        except(urllib2.URLError, urllib2.HTTPError):
            print("Failed to establish connection to "+url)
        else:
            # store the source and return it
            source = u.read()
            u.close()

        return source


    def _getDlLink(self, source):
        """ Extracts the direct download link of the book in the passed source """
        if not source or source.isspace():
            raise ValueError("Passed source is either empty or None! (_extractDownloadLink)")
        # filter out the link
        link = re.search("'http://filepi\.com/.+?'", source)
        if not link:
            raise ValueError("Couldn't find download link! (_extractDownloadLink)")
        # clean it up and return the link
        link = link.group().replace("'", "")
        return link


    def _getBookLinks(self):
        """ Extracts the links to the actual pages on which you find the download link for the book """
        # connect to the rss feed of it-ebooks.info
        source = self._getSource("http://feeds.feedburner.com/IT-eBooks?format=xml")
        doc = parseString(source) # parse the xml source
        xmlTag = doc.getElementsByTagName("feedburner:origLink") # extract all values of <link> elements
        # remove the tags from the extracted data
        links = [xmlTag[i].toxml().replace("<feedburner:origLink>","").replace("</feedburner:origLink>","") for i in range(1, len(xmlTag))]        
        return links


    def _addToVUrls(self, link):
        """ Adds the passed link to the list of visited urls """
        if link not in self._visitedUrls:
            self._visitedUrls.append(link)
        return


    def _getBookTitle(self, source):
        """ Filters out the book title of the passed source """
        if not source:
            raise ValueError("Passed source was empty or none! (_getBookTitle)")
        title = re.search("<h1\sitemprop=\"name\">.+?</h1>", source)
        if not title:
            raise ValueError("Failed to obtain the book title!")
        title = title.group().replace("<h1 itemprop=\"name\">", "").replace("</h1>", "")
        return title


    def _downloadFile(self, url, refUrl):
        """ Downloads the file at the given url, the passed refUrl is the referer address 
            which is needed to make use of the direct download feature of filepi. """
        if not url:
            raise ValueError("Can't download file, url is empty or None! (_downloadFile(url))")
        elif not refUrl:
            raise ValueError("Can't download file without the refering url parameter! (_downloadFile(.., refUrl))")
        try:
            u = urllib2.Request(url, None, {"User-Agent":self._userAgent, "Referer":refUrl, "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
            u = urllib2.urlopen(u)
    
            if u.code != 200:
                u.close() 
                raise urllib2.HTTPError("Status code wasn't positive! (_downloadFile)")
            data = u.read()
        except(urllib2.URLError, urllib2.HTTPError):
            print("Failed to download the file at {0}!".format(url))
        else:
            u.close()
            return data
        return


    def _saveFile(self, fname, data):
        """ Saves the passed file under the passed filename """
        # ensure that the directory exist before trying to write the downloaded file
        if os.path.isdir(self._savePath) is False:
            os.makedirs(self._savePath)
        
        # write the passed data to file
        with open(self._savePath + fname+".pdf", "w") as f:
            f.write(data)
        print("{0}.pdf has been saved!".format(fname))
        return


    def __del__(self):
        """ save the visited urls list to file """
        # if a list of visited urls already exists we append to it
        if os.path.isfile(self._visitedUrlsPath) is True:
            # read the list
            with open(self._visitedUrlsPath, "r") as f:
                storedUrls = [u.strip() for u in f.readlines()]
            # compare it with our non-file list
            with open(self._visitedUrlsPath, "a") as f:
                uniqueUrls = [x.strip() for x in self._visitedUrls if x not in storedUrls]
                for u in uniqueUrls:
                    f.write(u+os.linesep)
        else: 
            with open(self._visitedUrlsPath, "w") as f:
                for u in self._visitedUrls:
                    f.write(u+os.linesep)



if __name__ == "__main__":
    bg = BookGrab()
    bg.startGrabbing()