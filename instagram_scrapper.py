#Yenna Rascala

from bs4 import BeautifulSoup
import urllib2
import lxml
import json
import csv

a = list()
with open('url.txt', 'rU') as f:
	for line in f:
		response = urllib2.urlopen(line)
		html = response.read()    
		soup = BeautifulSoup(html,'lxml')
		d = soup.findAll('script')

		x = d[6].getText()
		x = x.replace('window._sharedData = ','')
		x = x[:-1]
		x = json.loads(x)
		
		username = x['entry_data']['ProfilePage'][0]['user']['username']
		followers = str(x['entry_data']['ProfilePage'][0]['user']['followed_by']['count'])
		posts = str(x['entry_data']['ProfilePage'][0]['user']['media']['count'])
		insta_id = str(x['entry_data']['ProfilePage'][0]['user']['id'])
		
		a.append(username)
		a.append(followers)
		a.append(posts)
		a.append(insta_id)
		
		with open("test.csv", "a") as fp:
			wr = csv.writer(fp, dialect='excel')
			wr.writerow(a)
		del a[:]