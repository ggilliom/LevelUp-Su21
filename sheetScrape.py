import bs4
import requests
from bs4 import BeautifulSoup

#FIND NEW SITE BECAUSE THIS ONE HAS RESTRICTED ACCESS...

#Populate w/ sites to scrape...
sitesList = ['https://www.kutasoftware.com/freeica.html']

#Populate w/ sites to scrape with their corresponding element to search...
sitesDict = {
    'https://www.kutasoftware.com/freeica.html' : 'pl-8',
    #...
}

def scrapeSite(index):

    fileList = []
    baseRating = "3"

    givenSite = sitesList[index]
    givenElement = sitesDict[givenSite]

    ourRequest = requests.get(givenSite)
    soup = bs4.BeautifulSoup(ourRequest.text, "html5lib")

    for linkElement in soup.find_all('li', {'class':givenElement}):
        urlText = linkElement.find('a')['href']
        name = urlText.split(' -')[1]

        ourTuple = (urlText, name, baseRating)
        fileList.append(ourTuple)

    return fileList

#All the links from this list are from the one site from sitesList...
importList = scrapeSite(0)
