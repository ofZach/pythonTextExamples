
import urllib
from bs4 import BeautifulSoup  
from subprocess import call
from Levenshtein import distance

#print distance("ahmed", "ahem sdflkjsadfklj")

# #sudo pip install python-Levenshtein
# #sudo pip install BeautifulSoup

# # ------------------------------- 
# # brew install wget
# # cnn image 
# # page = urllib.urlopen("http://www.cnn.com/").read()
# # soup = BeautifulSoup(page)
# # imgTags = soup.find_all('img')
# # for img in imgTags:
# # 	print img['src']
# # 	call(["wget", img['src']])

lookWords = []

def loadPage( urlToOpen ):
	page = urllib.urlopen(urlToOpen).read()
	soup = BeautifulSoup(page)
	aTags =  soup.find_all('a')
	for aTag in aTags:
		if "look"  in aTag.text:
			#print aTag.text
			lookWords.append(aTag.text)
		if ">>" in aTag.text:
			#print aTag.text
			url = "http://www.onelook.com" +  aTag["href"]
			loadPage(url)

loadPage("http://www.onelook.com/?w=*look*&ls=a")

#sort alphabetcially
#lookPhrases = sorted(lookPhrases)

currentWord = "look"

lookPhrasesStoredByDistance = []

while len(lookWords) > 0:

	smallestDiffWord = ""
	smallestDiff = 1000000
	
	for word in lookWords:
		edit_dist = distance(currentWord.encode('utf-8'), word.encode('utf-8'))
		if smallestDiff > edit_dist:
			smallestDiffWord = word
			smallestDiff = edit_dist
	
	currentWord = smallestDiffWord
	if smallestDiffWord in lookWords: lookWords.remove(smallestDiffWord)
	lookPhrasesStoredByDistance.append(smallestDiffWord)
	#print smallestDiffWord


outputFile = open("lookPhrasesSorted.txt", 'w')

for phrase in lookPhrasesStoredByDistance:
	outputFile.write(phrase.encode('utf-8'))
	outputFile.write("\n")

outputFile.close()









