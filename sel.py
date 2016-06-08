#!/usr/bin/env python
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://contests.covers.com/Survivor/Contestant/d48ff985-065e-e511-9e61-0024e8753722')
#driver.get('http://contests.covers.com/Survivor/Contestant/5493f985-065e-e511-9e61-0024e8753722')

searchBox = driver.find_element_by_id('txtSearch')

if "Next Pick Deadline" in driver.page_source:
	driver.quit()
else:	
	league = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(2)').text
	team = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(3)').text[:6]
	bet = driver.find_element_by_css_selector('table.cmg_contests_pendingpicks tr:nth-child(2) td:nth-child(6)').text
	searchBox.send_keys(bet)

	driver.get('http://www.sportsplays.com/login.html')
	
	config = open('../config.txt', 'r')
	
	username = driver.find_element_by_id('username')
	username.send_keys(config.readline())
	
	password = driver.find_element_by_id('password')
	password.send_keys(config.readline() + '\n')
	
	config.close()
	
	time.sleep(5)
	driver.get('http://www.sportsplays.com/make-pick.html')
	
	driver.find_element_by_link_text(league).click()

time.sleep(5)
driver.quit()
