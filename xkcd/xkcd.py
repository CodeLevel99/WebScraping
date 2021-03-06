#!/usr/bin/env python3

import requests, bs4, datetime

def getPage():
	"""
	Returns the request of specified URL.

	:returns: requests
	"""
	res = requests.get('http://www.xkcd.com')
	res.raise_for_status()
	return res

def createSoup(request):
	xkcdSoup = bs4.BeautifulSoup(request.text, 'html5lib')
	#get all elements with 'img'
	imgElems = xkcdSoup.select('#comic img')
	#get attribute of img elem
	url = imgElems[0].get('src')
	return url

def mkImgRequest(url):
	imgRes = requests.get('http:' + url)
	print("Downloading image from :" + url)
	return imgRes

#datetime object - gets today's date
today = datetime.date.today()

#stores request for page xkcd.com
page = getPage()

#stores the url of the xkcd comic for today
imgUrl = createSoup(page)

#store request for today's comic
image = mkImgRequest(imgUrl)

#format date string
todayExtension = today.strftime('%Y_%m_%d')

xkcd_comic = open('xkcd_' + todayExtension + '.png', 'wb')

for chunk in image.iter_content(100000):
	xkcd_comic.write(chunk)

xkcd_comic.close()



