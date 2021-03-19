import requests
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

#For Captchas
API_KEY = 'deadeba0a355a7279f678af3246f6e65'
data_sitekey = '33f96e6a-38cd-421b-bb68-7806e1764460'

# Tried the below to spoof the Capcha... didn't work
options = Options()
# ua = UserAgent(use_cache_server = False, verify_ssl = False)
# userAgent = ua.random
# options.add_argument(f'user-agent={userAgent}')

options.add_argument("--incognito")
options.add_argument("--window-size=1920x1080")

PATH = "/Users/spland/chromedriver"

# driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
driver = webdriver.Chrome(PATH)

URL = 'https://palmettostatearmory.com/shop-ammo-by-caliber.html'
driver.get(URL)

#Get all links in the page
ammoLinks = []
elementList = []
elems = driver.find_elements_by_xpath("//*[@href]")
for elem in elems:
  if("ammo" in elem.get_attribute("href")):
    ammoLinks.append(elem.get_attribute("href"))
    elementList.append(elem)

#Parse links to determine available calibers on PSA website and create a list with links + caliber name
outputLinks = []
outputElems = []
x = 0
for i in ammoLinks:
  s = i[32:]
  s = s.split(".",1)[0]
  s = s.split("-")
  if(bool(re.search(r'\d', s[0]))):
    outputLinks.append({'link': i+'?stock_filter=Show+Only+In+Stock', 'caliber': s[:-1]})
    outputElems.append(elementList[x])
  x+=1

# PSA 9mm ammo -- only retrieve what is in stock
#URL = 'https://palmettostatearmory.com/9mm-ammo.html?stock_filter=Show+Only+In+Stock'


# Might need to repeat the above process for reach caliber to determine products with that caliber... going to do a caliber with in stock ammo as a test run

#Idk how I'm going to get around the "are you human stuff"... worry about that later
#Sleeping, then getting another URL didn't work... going to try to click the element
#time.sleep(5)

#clicking still brings up "are you human bullshit"
#outputElems[55].click()

URL = outputLinks[55]['link']
time.sleep(5)
driver.get(URL)

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



#URL = 'https://palmettostatearmory.com/410-gauge-ammo.html?stock_filter=Show+Only+In+Stock'





