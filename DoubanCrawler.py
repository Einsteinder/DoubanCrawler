# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import expanddouban
import urllib
import csv

"""
return a string corresponding to the URL of douban movie lists given category and location. 
"""
def getMovieUrl(location,category):
	return "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,"+location+","+category 
#url = getMovieUrl("剧情","美国")

def get_html(url):
    f = open('htmlcode.txt','w')
    html = expanddouban.getHtml(url)
    f.write(html)
    f.close()
class Movie:
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link

"""
return a list of Movie objects with the given category and location. 
"""

def getMovies(location, category):
	movieList = []
	url = getMovieUrl(category, location)
	html = expanddouban.getHtml(url,True)
	soup = BeautifulSoup(html, 'html.parser')

	for link in soup.find_all('a',attrs={'class':'item'}):
		x = Movie(
		name = str(link.p.span.string),
		rate = str(link.find("span", class_="rate").string),
		location = location,
		category = category,
		info_link = str(link.get('href')),
		cover_link = str(link.div.span.img.get('src')))
		movieList.append(x)

	return movieList
def outPutCsv(location,category):
	movieList = getMovies(location,category)
	with open('movies.csv', 'a', newline='',encoding='utf-8-sig') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter="|",quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		for item in movieList:
			spamwriter.writerow([item.name+"|"+item.rate+"|"+item.location+"|"+item.category+"|"+item.info_link+"|"+item.cover_link])
#outPutCsv("美国","喜剧")

def outPutAllCsv():
	categoryList = ["爱情","喜剧","科幻","动作","悬疑","犯罪","恐怖","青春","励志","战争","文艺","黑色幽默","传记","情色","暴力","音乐","家庭"]
	locationList = ["大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","西班牙","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]
	for category in categoryList:
		for location in locationList:
			outPutCsv(location,category)
outPutAllCsv()
