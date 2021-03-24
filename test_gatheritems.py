import requests
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from PIL import Image # using this to display images I grab from products
from selenium.common.exceptions import NoSuchElementException


PATH = "/Users/spland/chromedriver"
driver = webdriver.Chrome(PATH)

URL = 'https://palmettostatearmory.com/12-gauge-ammo.html?stock_filter=Show+Only+In+Stock'
driver.get(URL)


elems = driver.find_elements_by_class_name('product-item-info')

productLinks = []
listings = []

# we have the whole product-item-info element, from there we can get the product-item-link element and then use getAttribute to get the href
# link inside of the product-item-link element
list_id = 0
for elem in elems:
  # this is the name of the product -- link = elem.find_element_by_class_name('product-item-link').text
  productLinks.append(elem.find_element_by_class_name('product-item-link').get_attribute('href')) # this works for getting product links
  # im = Image.open(requests.get(elem.find_element_by_class_name('product-image-photo').get_attribute('src'), stream=True).raw)
  # this shows the image captured above -- im.show()
  try:
    e_link = elem.find_element_by_class_name('product-item-link').get_attribute('href')
  except NoSuchElementException:
    e_link = None
  try:
    e_img = elem.find_element_by_class_name('product-image-photo').get_attribute('src')
  except NoSuchElementException:
    e_img = None
  try:
    e_name = elem.find_element_by_class_name('product-item-link').text
  except NoSuchElementException:
    e_name = None
  try:
    e_price = elem.find_element_by_class_name('special-price').text
  except NoSuchElementException: #add logic for when there is not speical price
    try:
      e_price = elem.find_element_by_class_name('price-wrapper').text
    except NoSuchElementException: #add logic for when there is not speical price
      e_price = None
  try: #xpath didn't work, but css_selector does - have to add dot before price wrapper.. the more you know
    e_unit = elem.find_element_by_css_selector('.price-wrapper.unit-price').text
  except NoSuchElementException:
    e_unit = None
 

  listings.append({'id': list_id, "link": e_link, "img": e_img, "name": e_name, "price": e_price, "p_per": e_unit})

  # listings.append({"id": list_id, "link": elem.find_element_by_class_name('product-item-link').get_attribute('href'), "img": elem.find_element_by_class_name('product-image-photo').get_attribute('src'),
  #   "name": elem.find_element_by_class_name('product-item-link').text, "price": elem.find_element_by_class_name('special-price').text, "p_per": elem.find_element_by_class_name('price-wrapper unit-price')})
  list_id+=1

print(listings)

# !!!! IMPORTANT - will need to run a hCaptcha on every new link because after testing, I don't think the answers are always the same

