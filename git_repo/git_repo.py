import sys
import requests
from bs4 import BeautifulSoup

def get_repo_count(userName):
	try :
		request=requests.get("https://github.com/"+userName+"?tab=repositories")
		folder="/"+userName+"?tab=repositories"
		soup=BeautifulSoup(request.text,"html.parser")
		divTag = soup.find_all("div", {"class": "user-profile-nav js-sticky top-0"})
		for divs in divTag:
			anchors=divs.find_all("a",{"href":folder})
			# spans=anchors.find_all("span")
			# print anchors.find('span').text
			for item in anchors:
				print item.text
	except Exception as exception:
		print(type(exception).__name__)

if not(len(sys.argv)==2):
	print("\nusage : python gitrepo.py 'username'\n")
else:
		get_repo_count(sys.argv[1])