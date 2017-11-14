from urllib.request import urlopen
from bs4 import BeautifulSoup
#收集所有内外链
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	bs0bj = BeautifulSoup(html)
	internalLinks = getInternalLinks(bs0bj, splitAddress(siteUrl)[0])
	externalLinks = getExternalLinks(bs0bj, splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print("获取的内链为"+link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

getAllExternalLinks("http://douyu.com") 