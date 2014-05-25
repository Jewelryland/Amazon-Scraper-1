from BeautifulSoup import BeautifulSoup as bs
import urllib2
import re


page = urllib2.urlopen(raw_input('enter the webpage:'))
prdct_page = bs(page)

def getlink():
    for a in prdct_page.findAll('a',href=True):
        match = re.search(r'product-reviews',a['href'])
        if match:
            matchtext = 'http://amazon.com'+match.string
            break
        pass
    return matchtext

reviewpage = urllib2.urlopen(getlink())
rev_page = bs(reviewpage)

def gettable(name, attr, tagid):
    global table
    table = rev_page.find(name,{attr : tagid})
    return table


def number_rev(revname,revattr,revtagid):
    revnum = table.findAll(revname, {revattr : revtagid})
    ratings = ['5 stars','4 stars','3 stars','2 stars','1 star']
    number = []
    for cell in revnum:
        celltext = cell.getText()
        celltext = celltext.strip("&nbsp;("+")")
        celltext = str(celltext)
        number.append(celltext)
        
    ratingsdict = dict(zip(ratings, number))
    print ratingsdict
    return ratingsdict
    
revtable = gettable('table','id',"productSummary")
number_rev('td','align',"right")


