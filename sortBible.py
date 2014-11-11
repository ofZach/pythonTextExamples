

# print "hello"
# words = ['hello','mom','how','are','you']
# print len(words)
# words = sorted(words)
# for word in words:
# 	print word

with open ("bible-kjv.txt", "r") as myfile:
	data=myfile.read()

words = data.split()

cleanWords = []

for word in words:
	word = word.strip()
	word = word.lower()
	cleanWords.append(word)


punctuations = '''0123456789!()-[]{};:'"\,<>./?@#$%^&*_~'''

superCleanWords = []

for word in cleanWords:
	noPunct = ""
	for char in word:
		if char not in punctuations:
			noPunct = noPunct + char
	if noPunct is not "":
		superCleanWords.append(noPunct)

superCleanWords = sorted(superCleanWords)

outputFile = open("biblesorted.txt", 'w')

for word in superCleanWords:
	outputFile.write(word + " ")

outputFile.close()

