import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs0bj = BeautifulSoup(html)
# 主对比表格是当前页面上的第一个表格
table = bs0bj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")
# 找到所有行标签

csvFile = open("../learngit/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
	for cell in row.findAll(['td', 'th']):
		#从行中知道所有表格头th，表格单元td，并循环
		csvRow.append(cell.get_text())
		writer.writerow(csvRow)
finally:
	csvFile.close()