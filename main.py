# So turns out you don't really need HTML Tidy at all.
import os
from bs4 import BeautifulSoup

def saveFile(fileName, stringToSave):
	dirToSave = os.path.dirname(os.path.abspath(__file__))
	newFile = open(dirToSave+'/'+fileName+".html", "w")
	newFile.write(stringToSave)
	newFile.close()

inputFile = open("messages.htm").read()
# document, errors = tidylib.tidy_document(inputFile)

#This builds the soup from the messages.html file
soup = BeautifulSoup(inputFile) #This method takes a while.

# This gives a list of all threads.
threads = soup.find_all('div', attrs={'class' : 'thread'})

names = []

def findNamesFromThread(thread):
	myList = thread.prettify().split(',')
	tmp = myList[0].split(" ")
	name1 = tmp[len(tmp)-2]+" "+tmp[len(tmp)-1]
	tmp = myList[1].split("\n")[0].split(" ")
	name2 = tmp[len(tmp)-2]+" "+tmp[len(tmp)-1]
	return (name1, name2)

#This gives you a list of all the thread names
for thread in threads:
	names.append(findNamesFromThread(thread)[1]) #Notice only name2 is taken

requiredName = "Eldan Cohen"

#This removes all threads other then one we ask for.
for thread in threads:
	if findNamesFromThread(thread)[1] != requiredName:
		thread.extract()

# This saves the formatted html to a new file; Notice the use of encode
saveFile("messagesAfterParse", soup.prettify().encode('utf-8'))