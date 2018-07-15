"""
This script will click on the share button to see who shared.
Then it will extract the name of everyone who has shared the post and store in a list.
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

#initializes the chrome driver, add options for a smooth scraping experience.
chrome_driver = r"C:\Users\mugen\PycharmProjects\chromedriver.exe"
options = Options()
options.add_argument('--disable-notifications')
prefs = {"profile.managed_default_content_settings.images":2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_driver, chrome_options=options)

# Goes to facebook
driver.get("https://www.facebook.com/")

# Logs me in
email = "email"
password = "pass"
loginelement = 'loginbutton'
emailelement = driver.find_element_by_name(email)
passwordelement = driver.find_element_by_name(password)
emailelement.send_keys("")
passwordelement.send_keys("")
loginelement = driver.find_element_by_id(loginelement).click()

# wait
time.sleep(3)

# search for the company
searchClass = '_1frb'
searchelement = driver.find_element_by_class_name(searchClass)
searchelement.send_keys('Glowsmile bulgaria' + "\n")
time.sleep(3)

# grab page
elem = driver.find_element_by_tag_name("body")

# Find the share link, page down twice to bring into view. Sloppy coding!
fbpage = 'GlowSmile Bulgaria'
fbpageelement = driver.find_element_by_link_text(fbpage).click()
time.sleep(3)
elem.send_keys(Keys.PAGE_DOWN)
elem.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
sharesbuttonclick = driver.find_element_by_class_name('UFIShareLink').click()

# Scrolls through all shares viewable according to certain users privacy settings
no_of_pagedowns = 500

while (no_of_pagedowns > 0):
    elem.send_keys(Keys.PAGE_DOWN)
    no_of_pagedowns-=1

# grab the html containing the usenames of those who shared the specific post
usertags = driver.find_elements_by_class_name('profileLink')

# Lure out the inner text (user name) from html
for i in range(0, len(usertags)):
    usertags[i] = usertags[i].text

updatedlist = list(set(usertags))

# display that list
for z in updatedlist:
    print(z)