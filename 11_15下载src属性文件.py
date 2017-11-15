import os 
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
# --------------没有检查，不要随意运行--------------

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
	if source.startswith("http://www."):
	# 以“http://www.”开头，则去掉开头加上“http://”赋给url
		url = "http://"+source[11:]
	elif source.startswith("http://"):
	# 以“http://”开头，则直接赋值给url
		url = source
	elif source.startswith("www."):
	# 以“www.”开头，则去掉开头加上“http://”赋值给url
		url = source[4:]
		url = "http://"+url
	else:
		url = baseUrl+"source"
	
	if baseUrl not in url:
	# 如果url的字符串中不包含“http://pythonscraping.com”字符串，则返回None
		return None
	return url
	# 返回包含baseUrl的地址，即获取绝对路径

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	# 获取下载路径
	path = absoluteUrl.replace("www.","")
	# 将绝对url中的"www."去掉并赋值给path
	path = path.replace(baseUrl,"")
	# 去掉路径中的“http://pythonscraping.com”部分
	path = downloadDirectory+path
	# 设置路径为“downloaded”+absoluteUrl的“www”之后的部分
	directory = os.path.dirname(path)
	# 返回一个上一层文件的目录名
	if not os.path.exists(directory):
	# 如果该目录名不存在，则生成新目录
		os.makedirs(directory)

	return path
	# 返回路径

html = urlopen("http://www.pythonscraping.com")
bs0bj = BeautifulSoup(html)
downloadList = bs0bj.findAll(src=True)
# 下载列表为html中所有属性src为True的标签。

for download in downloadList:
	fileUrl = getAbsoluteURL(baseUrl, download["src"])
	# 将带有src标签及“http://ww.pythonscraping.com”的地址赋值给fileUrl
	if fileUrl is not None:
		print(fileUrl)
		# 如果fileUrl存在，则打印文件地址

urlretrieve(fileUrl,getDownloadPath(baseUrl, fileUrl, downloadDirectory))
# 该方法为urllib模块中的函数，可以将远程数据下载到本地
# 将文件地址保存到本地路径