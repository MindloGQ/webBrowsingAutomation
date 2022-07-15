#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

baseUrl = 'http://192.168.11.206:8080/Supercar-Trader/'
url = 'http://192.168.11.206:8080/Supercar-Trader/home.do'
print('sending GET method to {}'.format(url))
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

pages = []
nextPages = []
next2Pages = []

for link in soup.find_all('a'):
    page = link.get('href')
    if page != '' and page != None and not page.endswith('.jsp'):
        pages.append(page)

pages = list(set(pages))

for page in pages:
    nextUrl = baseUrl+page
    print('sending GET method to {}'.format(nextUrl))
    nextReqs = requests.get(nextUrl)
    nextSoup = BeautifulSoup(nextReqs.text, 'html.parser')

    for nextLink in nextSoup.find_all('a'):
        nextPage = nextLink.get('href')
        if nextPage != '' and nextPage != None and not nextPage.endswith('.jsp'):
            nextPages.append(nextPage)

nextPages = list(set(nextPages))

for nextPage in nextPages:                    
    next2Url = baseUrl+nextPage
    print('sending GET method to {}'.format(next2Url))
    next2Reqs = requests.get(next2Url)
    next2Soup = BeautifulSoup(next2Reqs.text, 'html.parser')
    
    for next2Link in next2Soup.find_all('a'):
        next2Page = next2Link.get('href')
        if next2Page != '' and next2Page != None and not next2Page.endswith('.jsp'):
            next2Pages.append(next2Page)

next2Pages = list(set(next2Pages))

for next2Page in next2Pages:                    
    next3Url = baseUrl+next2Page
    print('sending GET method to {}'.format(next3Url))
    next3Reqs = requests.get(next3Url)