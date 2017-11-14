from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())	#生成随机路径防止反爬虫
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bs0bj = BeautifulSoup(html)
	return bs0bj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))	 #用正则表达式进行指定内容爬取
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)