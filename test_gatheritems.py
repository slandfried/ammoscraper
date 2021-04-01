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
from scraper import getLinks


def solveCaptcha(link, driver):
  #For Captchas
  API_KEY = '643ef18609fdca72440a9abbe8c5bd5f'

  #Found using inspect element on captcha page for 410 gauge
  data_sitekey = '33f96e6a-38cd-421b-bb68-7806e1764460'
  
  URL = link

  data_post = {'key': API_KEY, 'method': 'hcaptcha', 'sitekey': data_sitekey, 'pageurl': URL}
  captcha_id = requests.post(url = 'https://2captcha.com/in.php', data = data_post)
  # print(captcha_id)
  # print(captcha_id.text)
  time.sleep(15)
  data_get = {'key': API_KEY, 'action': 'get', 'id': captcha_id.text.split('|')[1]}
  answer = requests.get('https://2captcha.com/res.php', params = data_get).text

  if 'CAPTCHA_NOT_READY' in answer:
    time.sleep(5)
    data_get = {'key': API_KEY, 'action': 'get', 'id': captcha_id.text.split('|')[1]}
    answer = requests.get('https://2captcha.com/res.php', params = data_get).text
  answer = answer.split('|')[1]

  # send answer
  # IT WORKS!!!!!! - there was no g-recaptcha-response element, that's why original version from 2captcha website returned null element js error
  driver.execute_script("""
    let [answer] = arguments
    document.querySelector('[name="h-captcha-response"]').innerHTML = answer
    document.querySelector('.challenge-form').submit()
  """, answer)

def retrieveListings(id_num, link, driver):

  chrome_d = driver
  chrome_d.get(link)
  time.sleep(5)
  # need to determine if we've been re-directed to catpcha
  cap_stat = 1
  try:
    in_cap = driver.find_element_by_id("challenge-form")
  except NoSuchElementException:
    cap_stat = 0
  if(cap_stat):
    solveCaptcha(link, driver)
  list_id = id_num

  elems = chrome_d.find_elements_by_class_name('product-item-info')

  productLinks = []
  listings = []

  # we have the whole product-item-info element, from there we can get the product-item-link element and then use getAttribute to get the href
  # link inside of the product-item-link element
 
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
    list_id+=1 # ****** need to think about wtf I'm doing here with list_id
  
  return list_id, listings


def getData():
  URLs = getLinks()

  PATH = "/Users/spland/chromedriver"
  driver = webdriver.Chrome(PATH)

  num = 0
  outputList = []
  for u in URLs:
    results = retrieveListings(num, u["link"], driver)
    num = results[0]
    outputList.extend(results[1])
    time.sleep(5)
  return outputList








