from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# https://www.instagram.com/explore/tags/%EC%9E%90%EB%8F%99%EC%B0%A8/
base_url = "https://www.instagram.com/explore/tags/"
tag = input("Please enter the tag you want to search. ")
# quote_plus is convert the tag got from user to ascii value
url = base_url + quote_plus(tag)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)
# _aabd _aa8k _aanf -> has to replace the space( ) to dot(.)
instagram_picture = soup.select("_aabd._aa8k.aanf")
print(instagram_picture)
