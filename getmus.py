import requests
from urllib import request
from urllib import parse
import json

class Gmus(object):
	"""docstring for Gmus"""
	def __init__(self,mus_name):
			self.dowm = mus_name
			self.mus_name = str(mus_name)
			self.mus_name = parse.quote(self.mus_name.encode('utf8'))
			self.getlist(self.mus_name)
	def getlist(self,key):
		url = "http://search.kuwo.cn/r.s?client=kt&all=%s&pn=0&rn=10&uid=221260053&ver=kwplayer_\
		ar_99.99.99.99&vipver=1&ft=music&cluster=0&strategy=2012&encoding=utf8&rformat=json&vermerge=1&mobi=1" % key
		mlist = requests.get(url)
		res =json.loads(mlist.text)
		musid = res['abslist'][0]['MUSICRID'][6:]
		durl ="http://www.kuwo.cn/url?format=mp3&rid=%s&response=url&type=convert_url3&br=128kmp3&from=web" % musid
		mus_res = requests.get(durl)
		dowm =json.loads(mus_res.text)
		path = 'C:\\Users\\Administrator\\Desktop\\some\\py\\crawl\\mus\\'
		request.urlretrieve(dowm['url'], path+self.dowm+'.mp3')

# Gmus("老街")