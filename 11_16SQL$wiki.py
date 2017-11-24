from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

# 创建连接通道, 设置连接ip, port, 用户, 密码以及所要连接的数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='cjj0103', db='mysql', charset='utf8')
# conn为连接对象，cur为光标对象
cur = conn.cursor()
cur.execute('USE scraping')
# 执行语句

random.seed(datetime.datetime.now())

def store(title, content):
	cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title,content))
	# 在SQL中执行语句
	cur.connection.commit()
	# 连接确认，将信息传入数据库，再将信息插入数据库

def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bs0bj = BeautifulSoup(html)
	title = bs0bj.find("h1").get_text()
	content = bs0bj.find("div", {"id":"mw-content-text"}).find("p").get_text()
	store(title, content)
	# 把找到的标题、文本内容使用sotre函数传入数据库
	return bs0bj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
	while len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
		# 从所有内链中打开随机一个新内链
		print(newArticle)
		# 打印该内链
		links = getLinks(newArticle)
		# 不断查找
finally:
	cur.close()
	conn.close()