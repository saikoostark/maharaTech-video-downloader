from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube

import json
import re


def getyoutube(url):
	id = url.split('embed')[1][1:]
	print(id)

	video_link = f"https://www.youtube.com/watch?v={id}"
	return video_link

def solvecookies(cookies):
	# split the cookies string into individual cookies
	cookie_list = cookies.split('; ')

	# create a list to hold the cookies
	cookie_dicts = []

	# iterate over the cookie list and create a dictionary for each cookie
	for cookie in cookie_list:
		name, value = cookie.split('=', 1)
		cookie_dict = {'name': name, 'value': value}
		cookie_dicts.append(cookie_dict)
	return cookie_dicts




def getall(link, cookie):
	videos = []

	# set up the Selenium driver with a custom header containing cookies
	options = webdriver.ChromeOptions()
	# domain = "https://maharatech.gov.eg"

	cookies = solvecookies(cookie)
	driv = 'D:\\chromedriver.exe'
	options.add_argument(f"executable_path={driv}")

	driver = webdriver.Chrome(options=options)

	# define the URL to open
	url = link

	# open the URL in the Selenium driver
	driver.get(url)
	for cok in cookies:
		# cok['domain'] = domain
		driver.add_cookie(cok)
	driver.refresh()
	# get the page source and search for the pattern
	page_source = driver.page_source
	pattern = r"https://maharatech\.gov\.eg/mod/hvp/view\.php\?id=\d{3,5}"
	matches = re.findall(pattern, page_source)
	print(json.dumps(matches, indent=2), len(matches))
	# for each match, make another call and search for iframes containing YouTube links
	for match in matches:
		driver.get(match)
		sleep(3)
		iframe = driver.find_element(By.TAG_NAME, 'iframe')
		driver.switch_to.frame(iframe)
		iframe = driver.find_element(By.TAG_NAME, 'iframe')
		yout = getyoutube(iframe.get_attribute('src').split('?')[0])
		# download(yout)
		videos.append(yout)
		# sleep(1)
		print(json.dumps(videos, indent=2))


	# close the Selenium driver
	sleep(15)
	driver.quit()


cookies = r'_gcl_au=1.1.1078963054.1686847029; _scid=836ac3bf-3c57-4785-b7e5-5adc06943e7e; _fbp=fb.2.1686847036012.1401179849; _tt_enable_cookie=1; _ttp=ePb1tI0UbEQyeIuO7lyTntLGl9_; _gid=GA1.3.2034704322.1687338069; _sctr=1%7C1687381200000; MoodleSession=bec8ad91271abbc83e4fa6ac5a8f9dc3; MOODLEID1_=%25C4%2500%253B%253E%25CD%25E3%25001%25FC%252C%258C%255C; intelliboardPage=site; intelliboardParam=1; _ga_28R0GWMQZK=GS1.1.1687447003.13.1.1687447040.23.0.0; _scid_r=836ac3bf-3c57-4785-b7e5-5adc06943e7e; _ga_Y06GN5874R=GS1.1.1687447003.13.1.1687447040.0.0.0; _ga=GA1.1.464701991.1686847032; intelliboardTime=12'

getall('https://maharatech.gov.eg/course/view.php?id=790' , cookies)
