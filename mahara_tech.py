import re
import requests
from bs4 import BeautifulSoup
import json

header = {'cookie': '_gcl_au=1.1.1078963054.1686847029; _scid=836ac3bf-3c57-4785-b7e5-5adc06943e7e; _fbp=fb.2.1686847036012.1401179849; _tt_enable_cookie=1; _ttp=ePb1tI0UbEQyeIuO7lyTntLGl9_; _sctr=1%7C1686776400000; _gid=GA1.3.2034704322.1687338069; MoodleSession=5cbe4d55c2d973cf7628f9d054dd8b90; intelliboardPage=course; intelliboardParam=1438; _gat_gtag_UA_138951665_1=1; _gat_UA-103801499-2=1; _ga_28R0GWMQZK=GS1.1.1687372561.10.1.1687373911.60.0.0; _ga=GA1.1.464701991.1686847032; _scid_r=836ac3bf-3c57-4785-b7e5-5adc06943e7e; _ga_Y06GN5874R=GS1.1.1687372561.10.1.1687373912.0.0.0; intelliboardTime=3'}


def getyoutubelink(link):

	global header
	response = requests.get(link, headers=header)

	soup = BeautifulSoup(response.text, "html.parser")

	# Find the first iframe element with a src attribute that starts with "https://www.youtube.com/embed/"
	iframe = soup.findAll("iframe")
	print(iframe)

	# if iframe:
	# 	# Extract the video ID from the src attribute
	# 	video_id = iframe["src"].split("/")[-1].split("?")[0]
	# 	print(video_id)
	# else:
	# 	print("No YouTube video found on the page.")



def getebisode():
	# Replace the URL below with the webpage you want to parse
	url = "https://maharatech.gov.eg/course/view.php?id=1438"

	# Replace the pattern below with the regex pattern you want to match
	pattern = r"https://maharatech\.gov\.eg/mod/hvp/view\.php\?id=\d{5}"

	# Make a GET request to the webpage and parse its HTML content

	global header
	response = requests.get(url, headers=header)
	soup = BeautifulSoup(response.content, "html.parser")

	# Find all href attributes on the webpage and filter out those that don't match the pattern
	matching_hrefs = [a["href"] for a in soup.find_all("a", href=True) if re.match(pattern, a["href"])]

	# Print the matching hrefs
	print(json.dumps(matching_hrefs, indent=2), len(matching_hrefs) )
	for i in matching_hrefs:
		getyoutubelink(i)


getebisode()
