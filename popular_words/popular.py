from bs4 import BeautifulSoup
import requests
import re
from stop_words import get_stop_words
import operator
def remove_stop_words(sorted_word):
    stop_words = get_stop_words('en')
    List = []
    for key,value in sorted_word:
        if key not in stop_words:
            List.append(key)
    return List
def get_words(url):
	response=requests.get(url)
	plain_text=response.text
	soup = BeautifulSoup(plain_text,'lxml')
	List=[]
	for content in soup.find_all('p'):
		matter=content.text
		words=matter.lower().split() # will be able to sort it
		for word in words:
			word=re.sub('[^A-Za-z]+', '', word)
			if len(word)>0:
				List.append(word)
	return List

# item=map(str,input().split())
def main():
	print "Enter the topic you want to see realted item"
	item=raw_input()
	# print item
	url="https://en.wikipedia.org/wiki/"+item
	words=get_words(url)
	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word]=1
	sorted_word= sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
	sorted_word=remove_stop_words(sorted_word)
	# get top 10 words
	# print type(sorted_word)
	if(len(sorted_word)>10):
		sorted_word=sorted_word[:10]
	print "MOST 10 FREQUNTLY OCCURING WORDS ARE"
	for words in sorted_word:
		print words
if __name__=='__main__':
	main()
