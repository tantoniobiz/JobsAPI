
import bs4 as bs
import urllib.request

from bs4 import BeautifulSoup


sauce = urllib.request.urlopen('https://alto.com/careers').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.find_all('a'))

for url in soup.find_all("a"):
    print(url.get('href'))

#for paragraph in soup.find_all("p"):
#    print(paragraph.text)