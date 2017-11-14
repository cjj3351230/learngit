from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())	#生成随机路径防止反爬虫
pages = set()

#获取所有内链列表
def getInternalLinks(bs0bj, includeUrl):
	internalLinks = []
	#找出以“/”开头的内链接
	for link in bs0bj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):	
		if link.attrs['href'] is not None:	 #如果找到的链接存在
			internalLinks.append(link.attrs['href'])	#把该链接加入到internalLinks列表中
	return internalLinks 	#返回带有所有内链的列表

#获取所有外链列表
def getExternalLinks(bs0bj, excludeUrl):
	externalLinks = []
	#找出以http或www开头且不含当前url的链接
	for link in bs0bj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):	#找到bs0bj中属性不含excludeUrl的链接标签。link从中循环
		if link.attrs['href'] is not None:	 #如果找到的外链存在
			if link.attrs['href'] not in externalLinks:	    #如果找到的外链不在externalLinks列表中
				externalLinks.append(link.attrs['href'])	#向externalLinks列表中加入找到的外链
	return externalLinks 	#返回带有所有外链的列表

#对Url切片。将Url去掉http://并进行切片，返回一个有地址各部分内容的list（之后只会用到第一个“/”以前的url值，这里当做url0）
def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")	
	return addressParts

#获取随机外链。
def getRandomExternalLink(startingPage):
	html = urlopen(startingPage) 	#打开起始页面并赋值给html
	bs0bj = BeautifulSoup(html)	 	#用美丽汤转译
	externalLinks = getExternalLinks(bs0bj, splitAddress(startingPage)[0]) 		#引用获取外链函数，在bs0bj中找到所有属性不带有url0的链接并赋值给externalLinks
	if len(externalLinks) == 0: 	#如果链接标签都带有url0，即没有外链都是内链，则externalLinks列表中没有元素，长度为0
		internalLinks = getInternalLinks(bs0bj, startingPage)		#从起始页面中找到带有内链的标签并赋值给internalLinks
		return getExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)], splitAddress(startingPage)[0])	#从内链列表internalLinks中随机抽取一个打开并寻找该地址内的所有外链
	else:	#如果链接中有外链，即externalLinks长度不为0
		return externalLinks[random.randint(0, len(externalLinks)-1)]	#从外链列表externalLinks中随机返回一个外链

def followExternalOnly(startingSite):	#仅追踪外链
	externalLink = getRandomExternalLink("http://douyu.com")		#将得到的外链赋值给externalLink列表
	print("随机外链为："+externalLink)	#打印该随机外链
	followExternalOnly(externalLink)	#继续对该外链进行随机外链获取

followExternalOnly("http://douyu.com")

#第40行和第41行

