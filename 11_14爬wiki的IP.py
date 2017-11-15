from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bs0bj = BeautifulSoup(html)
	return bs0bj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
	# 返回所有不包含“：”的，在名为bodyContent区中的链接

def getHistoryIPs(pageUrl):
	# 编辑历史页面RUL链接格式是：
	# http://en.wikipedia.org/w/index.php?title_in_URL&action=history
	pageUrl = pageUrl.replace("/wiki/", "")
	historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
	print("history url is: "+historyUrl)
	html = urlopen(historyUrl)
	bs0bj = BeautifulSoup(html)
	# 找出class属性是“mw-anonuserlink”的链接
	# 他们用IP地址代替用户名
	ipAddresses = bs0bj.findAll("a", {"class":"mw-anonuserlink"})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

links = getLinks("/wiki/Python_(programming_language)")
# 获取这个URL中名为bodyContent区的所有不包含“：”的链接

while len(links) > 0 :
# 当有链接时
	for link in links:
		print("---------------------------------")
		historyIPS = getHistoryIPs(link.attrs["href"])
	# 找到所有不含“：”的链接href属性中的链接并代入getHistoryIPs函数，获取这些链接中class为“mv-anonuserlink”的内容，并获取文本放入addressList并返回
	# 最终存入historyIPS中
		for historyIP in historyIPS:
			print(historyIP)

	newLink = links[random.randint(0, len(links)-1)].attrs["href"]
	# 在所有找到不含“：”的链接中，随机获取任意一个链接的“href”属性并付给newLink
	links = getLinks(newLink)
	# 将新链接打开后查找该链接中不包含“：”的链接，并循环查找，获取IP地址，赋值给historyIP并打印