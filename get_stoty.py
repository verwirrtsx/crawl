import requests
from urllib import parse
from urllib import request
from lxml import etree

class Getsotry(object):
	"""docstring for Getsotry"""
	def __init__(self,stoty_name):
		self.headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
		}
		self.dowm = stoty_name
		self.stoty_name = str(stoty_name)
		self.stoty_name = parse.quote(self.stoty_name.encode('gbk')) 
		# print(self.stoty_name)
		self.url = 'https://www.qb5.tw/modules/article/search.php?searchtype=articlename&searchkey=' + self.stoty_name
		self.goMenu()
	def goMenu(self):
		r = requests.get(self.url,headers=self.headers)
		tree = etree.HTML(r.text)
		table_all = tree.xpath('//tr/td[1]/a/@href')
		if table_all:
			for x in table_all:
				url = 'https://www.qb5.tw' + x
				self.getMenu(url)
		else :
			self.getMenu(self.url)
	def getMenu(self,url):
		re = requests.get(url)
		etree_h = etree.HTML(re.text)
		t_list = etree_h.xpath('/html/body/div[4]/dl/dd/a/@href')
		for i in t_list:
			url = 'https://www.qb5.tw' + i
			res = requests.get(url)
			res.encoding='gbk'
			tree1 = etree.HTML(res.text)
			content = tree1.xpath('//*[@id="content"]/text()')
			strr = ','.join(content)
			try:
				with open('%s.txt' % self.dowm,'a+', encoding='utf8') as f:
					f.write(strr)
			except :
				return False
		return True

		# /html/body/div[4]/dl/dd/a/@href
	# def get(self):
	# 	str2 = parse.quote(self.stoty_name.encode('gb2312')) 
	# 	print(str2)
	# def set(self):
	# 	str2 = parse.unquote(self.stoty_name)
	# 	print(str2)