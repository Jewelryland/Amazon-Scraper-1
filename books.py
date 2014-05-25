from BeautifulSoup import BeautifulSoup as bs
import requests
import re

page = requests.get(raw_input('enter the webpage: '))
prdct_page = bs(page.content)

findbooks = prdct_page.findAll('a',{'class':"sim-img-title"})
bookstring = str(findbooks)
booksoup = bs(bookstring)

class otherbooks(object):

    def __init__(self):
        self.otherbooks = []
        self.cleanbooks = []

    def alsobought(self):

        alsoboughtlist = []

        for a in booksoup.findAll('a',href=True):
            url_end = a['href']
            alsoboughtlist.append(url_end)
            pass
        self.otherbooks = alsoboughtlist
        return self.otherbooks

    def completeurl(self):
        cleanedlist = []
        for i in self.otherbooks:
            i = "http://www.amazon.com" + i
            cleanedlist.append(i)
            pass
        self.cleanbooks = cleanedlist
        print self.cleanbooks
        return self.cleanbooks

test = otherbooks()

test.alsobought()
test.completeurl()
