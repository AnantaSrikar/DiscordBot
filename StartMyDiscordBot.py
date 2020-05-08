# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:44:55 2019

@author: ANANTA SRIKAR
"""
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument, CommandNotFound
import requests
import os
from json import load

os.chdir(os.path.dirname(os.path.abspath(__file__))) #making the file work from anywhere

def tokens():
	with open("res/TOKENS.json", 'r') as FPtr:
		return load(FPtr)

def NewsFromBBC(): 

	main_url = tokens()["int_news_url"]
 
	open_bbc_page = requests.get(main_url).json() 
 
	article = open_bbc_page["articles"] 

	results = [] 
	data = ''
	  
	for ar in article: 
		results.append(ar['title']) 
		  
	for i in range(len(results)): 
		data = data + str(i+1) + ') ' + str(results[i]) + '\n'
	
	return data

def indianNews():
	
	main_url = tokens()["ind_news_url"]

	news = requests.get(main_url).json()

	article = news["articles"]

	results = [] 
	data = ''
	  
	for ar in article: 
		results.append(ar['title']) 
		  
	for i in range(len(results)): 
		data = data + str(i+1) + ') ' + str(results[i]) + '\n'
	
	return data

def return_weather(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, tokens()["weather_token"])

	res = requests.get(url)

	data = res.json()

	try :
		temp = data['main']['temp']
		wind_speed = data['wind']['speed']
		description = data['weather'][0]['description']
		data = 'Weather in {} :\n'.format(city) + 'Temperature : {} °C\n'.format(temp) + 'Wind Speeds : {} m/s\n'.format(wind_speed) + 'Description : {}'.format(description)

	except KeyError :
		data = 'Please enter a valid city name'

	return data

bot = commands.Bot(command_prefix='>')
bot.remove_command("help")

@bot.event
async def on_ready():  
	print("\nLogged in as:\t{}".format(str(bot.user)))
	print("------------------")

	if(not hasattr(bot, 'appInfo')):
		bot.appInfo = await bot.application_info()    
		global owner
		owner = bot.appInfo.owner

@bot.command(name = 'start')
async def ping(ctx):
	await ctx.channel.send("Hey {} . I'm still awake btw....".format(ctx.message.author.mention) )

@bot.command(name = 'help')
async def helpHim(ctx):
	async with ctx.channel.typing():
		fileManager = open('res/bot_intro.txt', 'r')
		bot_intro = fileManager.read()
		bot_intro = bot_intro.replace('Srikar', owner.mention)
		fileManager.close()
		await ctx.channel.send(bot_intro)

@bot.command()
async def send_message(ctx, *, message : str):
	await ctx.channel.send(message)

@bot.command(name = 'weatherUpdate')
async def send_weather(ctx):
	city = ctx.message.content[15:]
	await ctx.channel.send(return_weather(city))

@bot.command(name = 'intNews')
async def send_int_news(ctx):
	async with ctx.channel.typing():
		await ctx.channel.send(NewsFromBBC())

@bot.command(name = 'indNews')
async def send_ind_news(ctx):
	async with ctx.channel.typing():
		await ctx.channel.send(indianNews())
	
@bot.command(name = 'owner')
async def send_owner(ctx):
	await ctx.channel.send('{} owns me. Literally!'.format(owner.mention))

@bot.event
async def on_message(message):

	msg = message.content.lower()

	if(message.author != bot.user and not(message.author.bot)):

		if ((msg.startswith('hi') or msg.startswith('hey') or msg.startswith('sup'))) :
			await message.channel.send("Wassup {}".format(message.author.mention))   # never directly do message.channel.send() as it will go to infinity loop
		
		elif ((msg.startswith('gn') or 'good night' in msg)):
			await message.channel.send("Good Night {}".format(message.author.mention) )
		
		elif ('boomer' in msg):
			await message.channel.send(file = discord.File('res/ok_boomer.jpg') )
		
		elif ('bye' in msg):
			await message.channel.send('Goodbye {}'.format(message.author.mention))

		if(message.author == owner):
			#print('My owner has sent a message!') ---> do something which owner only has access to
			pass # don't forget to remove this after adding a function

		await bot.process_commands(message)

@bot.event
async def on_member_remove(member):
	await member.guild.system_channel.send("{} has left {}".format(member.mention, member.guild.name)) # TODO : shows invalid-user when banned

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		await ctx.channel.send("Sorry {} ! I still don't know that command 😞\nTry `>help` to see what I can do.".format( ctx.message.author.mention) )

bot.load_extension('cogs.testCog')
bot.load_extension('cogs.managementCog')
bot.load_extension('cogs.ownerCog')
bot.load_extension('cogs.covCog')

bot.run(tokens()["bot_token"])
#nothing will run after this command ;)

# TODO : set_permissions() if command is sent by admin
# TODO : add unban
# TODO : add timed messages when nobody is chatting
# TODO : Fix bug when someone says yeah
# TODO : mute members on a channel