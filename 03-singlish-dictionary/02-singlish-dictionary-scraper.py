from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import string
import nltk;

from nltk.tokenize import word_tokenize, sent_tokenize;

url = "http://www.mysmu.edu/faculty/jacklee/singlish_";
alphabets = string.ascii_lowercase

final_content = []

for i in range(0, 26):
	myurl = url + alphabets[i] + ".htm"
	print(myurl);
	chrome = webdriver.Chrome()
	driver = chrome
	driver.get(myurl)

	delay = 3 # seconds
	try:
		myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body')))
		print("Page is ready!")
	except TimeoutException:
		print("Loading took too much time!")


	content = driver.find_elements_by_tag_name("p")
	for definition in content:
		final_content.append(definition.text);
	time.sleep(5)
	driver.quit()

qq = pd.DataFrame(final_content)

qq.to_csv("singlish.csv")