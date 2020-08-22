import feedparser
from datetime import datetime
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


from urllib.request import Request, urlopen

import re

from django.db import models


def get_feeds():
	print("Parsing..")
	NewsFeed = feedparser.parse("https://udemycoupon.learnviral.com/feed/?post_type=coupon")
	return NewsFeed.entries

def parse(link):
    print("Get Url, image..")
    while True:
        try:
            fp = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        except Exception as inst:
            print("Faile",link)
        finally:
	        mybytes = urlopen(fp).read()

        	parsed_html = BeautifulSoup(mybytes.decode("utf8"),features="html5lib")
        	udemy = parsed_html.body.find('div', attrs={'class':'link-holder'}).contents[1]
        	udemy_img_code = parsed_html.body.find('div',attrs={'class':'store-image'})

        	udemy_url = re.search("(?P<url>https?://[^\s]+)",str(udemy)).group("url")
        	udemy_img = re.search("(?P<url>https?://[^\s]+.jpg|.png|.jpeg|.svg)",str(udemy_img_code)).group("url")
        	return (udemy_url,udemy_img)

def get_description(link):
    #div js-simple-collapse js-simple-collapse--description
	fp = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	mybytes = urlopen(fp).read()

	parsed_html = BeautifulSoup(mybytes.decode("utf8"),
		features="html5lib")
	udemy_desc = parsed_html.body.find('div', attrs={'class':'bottom-container'}).contents[1]
	return str(udemy_desc)

def get_posts():
	feeds = get_feeds()
	posts = []
	print("Add feeds to dict...")
	for feed in feeds:
		link , image= parse(feed.link)
		print("PARSE DONE")
		slug=str(feed.title).replace('[Free] ','')
		slug=re.sub("[^A-Za-z0-9]", " ", slug.strip())
		slug=' '.join(slug.split())
		if len(slug) < 5:
			now = datetime.now()
			tm= datetime.timestamp(now)
			slug=slug+("-%d"%tm)
		slug = str(slug).replace(' ', '-').lower()
		if slug.startswith('the-'):
			slug = slug[4:]
		slug = ''.join(e for e in slug if e.isalnum() or e == '-')
		#body = feed.summary
		#body = re.sub('<a.*?</a>', '', body)
		#body = re.sub(' Published by:.*?</p>', '', body)
		#body = re.sub('<p>For more:.*?</p>', '', body)
		print("DESC-")
		body = get_description(link)
		print("DESC")
		posts.append({
			'title': str(feed.title).replace('[Free] ',''),
			'body': body,
			'link':  link[:-1],
			'image': image,
			'status': 'published',
			'slug': slug
			})
	return posts



from blog.models import Post
import urllib.request

import os
from urllib.parse import urlparse
from cms0.settings import MEDIA_URL, BASE_DIR

def save_post(title,body,link,image,status,slug):
	i = 0
	img_name = os.path.basename(urlparse(image).path)
	db_img = "posts/"+img_name
	img_name = BASE_DIR+"/static_cdn"+MEDIA_URL+"posts/"+img_name
	try:
		urllib.request.urlretrieve(image,img_name)
	except Exception as e:
		print(title)
	finally:
		if not Post.objects.filter(title=title).exists():
			i = 1
			re = Post(title=title,
			body=body,
			link=link,
			image=db_img,
			status=status,
			slug=slug)
			re.save()
		return i

def start():
	i=0
	feeds = get_posts()
	print("Saving posts...")
	for post in feeds:
		i+=save_post(**post)
	print("Done! {} of {} posts".format(i,len(feeds)))

start()
