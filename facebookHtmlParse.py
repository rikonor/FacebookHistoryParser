# So turns out you don't really need HTML Tidy at all.
import os
from bs4 import BeautifulSoup

class facebookHtmlParse(object):
	def loadString(self, fileString):
		self.inputFile = fileString

	def buildSoup(self):
		self.soup = BeautifulSoup(self.inputFile) #This method takes a while.

	def buildThreads(self):
		self.threads = self.soup.find_all('div', attrs={'class' : 'thread'})

	def findNamesFromThread(self, thread):
		myList = thread.prettify().split(',')
		tmp = myList[0].split(" ")
		name1 = tmp[len(tmp)-2]+" "+tmp[len(tmp)-1]
		tmp = myList[1].split("\n")[0].split(" ")
		name2 = tmp[len(tmp)-2]+" "+tmp[len(tmp)-1]
		return (name1, name2)

	def getNamesList(self):
	#This gives you a list of all the thread names
		names = []
		for thread in self.threads:
			names.append(self.findNamesFromThread(thread)[1]) #Notice only name2 is taken
		return names

	def extractRequired(self, requiredNames):
		for thread in self.threads:
			if self.findNamesFromThread(thread)[1] not in requiredNames:
				thread.extract()
		# Remove nav-bar
		self.soup.find('div', attrs={'class' : 'nav'}).extract()
		return self.soup.prettify().encode('utf-8')

def saveFile(fileName, stringToSave):
	dirToSave = os.path.dirname(os.path.abspath(__file__))
	newFile = open(dirToSave+'/'+fileName+".html", "w")
	newFile.write(stringToSave)
	newFile.close()