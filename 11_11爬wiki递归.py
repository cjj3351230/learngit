from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())	#生成随机路径防止反爬虫
pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bs0bj = BeautifulSoup(html)

	try:
		print(bs0bj.h1.get_text())
		print(bs0bj.find(id="mw-content-text").findAll("p")[0])
		print(bs0bj.find(id="ca-edit").find("span").find("a").attrs["href"])
	except AttributeError:
		print("缺少属性，没事")

	for link in bs0bj.findAll("a", href=re.compile("^(/wiki/)")):	#找到bs0bj所有href属性中有/wiki/的标签
		if 'href' in link.attrs:	#如果link的属性中有href属性
			if link.attrs['href'] not in pages:	#如果这个链接的href属性没有爬取过
				newPage = link.attrs['href']	#将爬取属性中的链接给Newpage变量
				print("-------------------------\n"+newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")