import discord 
from discord.ext import commands
import requests
import json

curData_url = 'https://v1.api.covindia.com/covindia-raw-data'  #CovIndia API, the best data for India! Checkout covindia.com
allData = {}
class covCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command('covid')
	async def covidAllData(self, ctx):
		await ctx.channel.send(getTotalData())
	
	@commands.command('covidState')
	async def covidState(self, ctx):
		await ctx.channel.send(getStateData())

def reloadData():
	apiData = requests.get(curData_url).json()
	global allData 
	allData = {}
	for entry in apiData:
		if apiData[entry]['state'] in allData:
			if apiData[entry]['district'] in allData[apiData[entry]['state']]:
				allData[apiData[entry]['state']][apiData[entry]['district']]['infected'] += apiData[entry]['infected']
				allData[apiData[entry]['state']][apiData[entry]['district']]['dead'] += apiData[entry]['death']
			else:
				allData[apiData[entry]['state']][apiData[entry]['district']] = {}
				allData[apiData[entry]['state']][apiData[entry]['district']]['infected'] = apiData[entry]['infected']
				allData[apiData[entry]['state']][apiData[entry]['district']]['dead'] = apiData[entry]['death']
		else:
			allData[apiData[entry]['state']] = {}
			allData[apiData[entry]['state']][apiData[entry]['district']] = {}
			allData[apiData[entry]['state']][apiData[entry]['district']]['infected'] = apiData[entry]['infected']
			allData[apiData[entry]['state']][apiData[entry]['district']]['dead'] = apiData[entry]['death']

def getTotalData():
	reloadData()
	totalInfected = 0
	totalDead = 0
	for stateBoi in allData:
		for districtBoi in allData[stateBoi]:
			totalInfected += allData[stateBoi][districtBoi]['infected']
			totalDead += allData[stateBoi][districtBoi]['dead']
	return 'Total cases in India :\nInfected : {}\nDead : {}'.format(totalInfected, totalDead)

def getStateData():
	reloadData()
	returnText = 'State-wise count :\n'
	for stateBoi in allData:
		stateInfected = 0
		stateDead = 0
		for districtBoi in allData[stateBoi]:
			stateInfected += allData[stateBoi][districtBoi]['infected']
			stateDead += allData[stateBoi][districtBoi]['dead']
		returnText += '{}:\nInfected : {}\nDead : {}\n\n'.format(stateBoi, stateInfected, stateDead)
	return returnText


def setup(bot):
	bot.add_cog(covCog(bot))