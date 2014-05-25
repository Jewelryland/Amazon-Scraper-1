from BeautifulSoup import BeautifulSoup as bs
import requests
import re

page = requests.get(raw_input('enter the webpage: '))
prdct_page = bs(page.content)


class Prdct_Info(object):

    def __init__(self):

        self.cleanlist = []
        self.title = ''
        self.author = ''

    def parse_deets(self):

        find_deets = prdct_page.findAll('table',{'id':"productDetailsTable"})
        deet_soup = bs(str(find_deets))

        templist = []

        for cell in deet_soup.findAll('li'):
            cellcont = cell.text
            templist.append(cellcont)
            pass
        templist = templist[0:6] #the findAll('li') returns some text
        self.cleanlist = templist #that we don't want, so we change the list to
                                  #only include the desired text
        return self.cleanlist

    def bookname(self):
        title = prdct_page.find('span',{'id':"productTitle"})
        titlesoup = bs(str(title))
        titlename= titlesoup.text
        self.title = titlename
        return self.title

    def authorname(self):
        author = prdct_page.find('span',{'class':"bxgy-byline-text"})
        author = author.string
        author = author.strip('by ')
        self.author = author
        return self.author

test = Prdct_Info()
details = test.parse_deets()
booktitle = test.bookname()
name = test.authorname()
print details
print booktitle
print name
