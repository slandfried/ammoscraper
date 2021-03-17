import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

PATH = "/Users/spland/chromedriver"

driver = webdriver.Chrome(PATH)

URL = 'https://palmettostatearmory.com/shop-ammo-by-caliber.html'
driver.get(URL)

#Get all links in the page
ammoLinks = []
elems = driver.find_elements_by_xpath("//*[@href]")
for elem in elems:
  if("ammo" in elem.get_attribute("href")):
    ammoLinks.append(elem.get_attribute("href"))

#Parse links to determine available calibers on PSA website and create a list with links + caliber name
outputLinks = []
for i in ammoLinks:
  s = i[32:]
  s = s.split(".",1)[0]
  s = s.split("-")
  if(bool(re.search(r'\d', s[0]))):
    outputLinks.append({'link': i, 'caliber': s[:-1]})

# PSA 9mm ammo -- only retrieve what is in stock
#URL = 'https://palmettostatearmory.com/9mm-ammo.html?stock_filter=Show+Only+In+Stock'


