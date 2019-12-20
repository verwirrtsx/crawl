import requests
from urllib import parse
from urllib import request
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyperclip

class Movie(object):
	def __init__(self, movie_name):
		self.headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
		}
		self.movie_name = str(movie_name)
		self.movie_name = parse.quote(self.movie_name.encode('gbk')) 
		# print(self.stoty_name)
		self.url = 'http://s.ygdy8.com/plus/so1.php?typeid=1&keyword=' + self.movie_name
		self.goMenu(self.url)
	def goMenu(self,url):
		r = requests.get(url)
		r.encoding = 'gbk'
		mtree = etree.HTML(r.text)
		mlist = mtree.xpath('//table/tr[1]/td[2]/b/a')
		url_list =  mtree.xpath('//table/tr[1]/td[2]/b/a/@href')
		no = 0
		for x in mlist:
			title = x.xpath('string(.)')
			print('编号 %s %s' % (no,title))
			no +=1
		mno = input('请输入下载编号：')
		# mno=0
		read_url = 'http://s.ygdy8.com/'+ url_list[int(mno)]

		chrome_options = Options()
		chrome_options.add_argument('headless')
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(read_url)
		down_url = driver.find_element_by_xpath('//*[@id="Zoom"]/span/table[1]/tbody/tr/td/a').get_attribute('outerHTML')
		sta_no = down_url.index('thunder:')
		last = down_url[sta_no:-1]
		eno_no = last.index('">ftp')
		last = last[0:eno_no]
		pyperclip.copy(last)
		spam = pyperclip.paste()
		driver.close()
		# print(res)
		# requests模块测试
		# re = requests.get(read_url)
		# re.encoding = 'gbk'
		# dtree = etree.HTML(re.text)
		# with open('a.txt','a') as f:
		# 	f.write(down_url)
		# down_url = dtree.xpath('//*[@id="Zoom"]/span/table/tbody/tr/td/a/@*')
if __name__ == '__main__':
	movie = input('亲输入电影名字：')
	Movie(movie)