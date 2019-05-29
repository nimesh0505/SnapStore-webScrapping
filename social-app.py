import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import csv

appname=[]
appdesc=[]
applink=[]
appcategory='social';
page=1
while(page<3):
	url = "https://snapcraft.io/search?category=social&page="+str(page)
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"html.parser")

	for i in soup.findAll('a',attrs={'class':'p-media-object'},href=True):
		if i.text: 
			url1 ="https://snapcraft.io"+i['href']
			response = requests.get(url1)
			soup = BeautifulSoup(response.text,"html.parser")
			for i in soup.findAll('div',attrs={'class':'p-snap-heading'}):
				appname.append(i.find('h1').text)
			for j in soup.findAll('h4',attrs={'data-live':'summary'}):
				appdesc.append(j.text)
			for k in soup.findAll('div',attrs={'class':'p-code-snippet'}):
				a = k.find('input')['value']
				myString = re.sub(r"[\n\t]*", "",a)
				applink.append(myString)

	page=page+1			

with open('social.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    for i in range(len(appname)):
   		writer.writerow([i+1,appname[i],appdesc[i],applink[i],appcategory])

		


	