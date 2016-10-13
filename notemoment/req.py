__author__ = 'zhangtianren'
from bs4 import BeautifulSoup
import requests
r = requests.get('http://catalogue.uci.edu/allcourses/')
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text

a=[3,4,2,3,2]

soup=BeautifulSoup(r.content,"html.parser")
print(soup.li)