#!/usr/bin/env python
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#driver.get('http://contests.covers.com/Survivor/Contestant/d48ff985-065e-e511-9e61-0024e8753722')
driver.get('http://contests.covers.com/Survivor/Contestant/30a35d86-065e-e511-9e61-0024e8753722')

if "Next Pick Deadline" in driver.page_source:
	driver.quit()
else:		
	league = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(2)').text
	team = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(3)').text[:6]
	bet = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(6)').text

	driver.get('http://www.sportsplays.com/login.html')

	config = open('../config.txt', 'r')
	
	credentials = config.read().splitlines()

	config.close()

	username = driver.find_element_by_id('username')
	username.send_keys(credentials[0])	

	password = driver.find_element_by_id('password')
	password.send_keys(credentials[1] + '\n')

	time.sleep(5)

	driver.get('http://www.sportsplays.com/make-pick.html')

	driver.find_element_by_link_text(league).click()

	time.sleep(5)
	driver.quit()
