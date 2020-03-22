import discord 
from discord.ext import commands
import requests
import PyPDF2

dataList = []

class covCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command('covid')
	async def tester(self, ctx):
		await ctx.channel.send(getInfo())

def setup(bot):
	bot.add_cog(covCog(bot))

def getInfo():

	global dataList
	getDataList()

	fetchFromURL(True)

	if(isPDF()):
		for i in range(len(dataList)):
			dataList[i] += 1
		updateDataList()
		
	else:
		fetchFromURL(False)

	return retDataPDF()

def fetchFromURL(adder):
	if(adder):
		url = 'https://www.who.int/docs/default-source/coronaviruse/202003{}-sitrep-{}-covid-19.pdf'.format(dataList[0] + 1, dataList[1] + 1)
	else:
		url = 'https://www.who.int/docs/default-source/coronaviruse/202003{}-sitrep-{}-covid-19.pdf'.format(dataList[0], dataList[1])
	myfile = requests.get(url)
	open('res/testfile.pdf', 'wb').write(myfile.content)    

def getDataList():
	fileManager = open('res/urlData.txt', 'r')
	dataText = fileManager.read()
	global dataList
	dataList = dataText.split('\n')
	for i in range(len(dataList)):
		try:
			dataList[i] = int(dataList[i])
		except ValueError:
			pass

def updateDataList():
	fileManager = open('res/urlData.txt', 'w')
	dataText = ''
	global dataList
	for i in range(len(dataList)):
		dataText = dataText + str(dataList[i]) + '\n'
	fileManager.write(dataText)
	fileManager.close()

def retDataPDF():
	
	pdfFileObj = open('res/testfile.pdf', 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	pageObj = pdfReader.getPage(4)
	data = pageObj.extractText()
	simplifiedData = data.split('\n')
	
	emptySpace = ' '
	for emptySpace in simplifiedData:
		try:
			simplifiedData.remove(' ')
		except ValueError:
			pass
	indiaIndex = simplifiedData.index('India')
	textdata = 'Data for India :\n' + 'Total Confirmed Cases = {}\nTotal Confirmed new cases = {}\nTotal Deaths = {}\nTotal new Deaths = {}\nTransmission Classification : {}\nDays since last report case : {}'.format(simplifiedData[indiaIndex + 1], simplifiedData[indiaIndex + 2], simplifiedData[indiaIndex + 3], simplifiedData[indiaIndex + 4], simplifiedData[indiaIndex + 5], simplifiedData[indiaIndex + 6])
	pdfFileObj.close()

	return textdata
	#print(pdfReader.numPages)
def isPDF():
	try:
		pdfFileObj = open('res/testfile.pdf', 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		return True
	except PyPDF2.utils.PdfReadError:
		return False