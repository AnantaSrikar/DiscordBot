# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:44:55 2019

@author: ANANTA SRIKAR
"""
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument
import requests

tokens = []

#owner id = 605674719731253263

def getTokens():
    fileManager = open('res/TOKENS.txt', 'r')  #make the file in such a way that token[0] is for news, token[1] for weather, token[2] for bot
    tokenText = fileManager.read()
    global tokens
    tokens = tokenText.split('\n')

def NewsFromBBC(): 

    # BBC news api 
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={}".format(tokens[0])
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 

  
    # empty list which will  
    # contain all trending news 
    results = [] 
    data = ''
      
    for ar in article: 
        results.append(ar['title']) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        #print(i + 1, results[i])
        data = data + str(i+1) + ') ' + str(results[i]) + '\n'
    
    return data

def indianNews():
    
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(tokens[0])

    news = requests.get(main_url).json()

    article = news["articles"]

    results = [] 
    data = ''
      
    for ar in article: 
        results.append(ar['title']) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        #print(i + 1, results[i])
        data = data + str(i+1) + ') ' + str(results[i]) + '\n'
    
    return data

def return_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, tokens[1])

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

getTokens()
bot = commands.Bot(command_prefix='>')
bot.remove_command("help")

@bot.event
async def on_ready():
	print ("\nLogged in as:\t" + str(bot.user))
	print ("-----------------")

@bot.command(name = 'start')
async def ping(ctx):
    await ctx.channel.send("Hey " + ctx.message.author.mention + ". I'm still awake btw....")

@bot.command(name = 'help')
async def helpHim(ctx):
    async with ctx.channel.typing():
        fileManager = open('res/bot_intro.txt', 'r')
        bot_intro = fileManager.read()
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

@bot.command(name = 'members')
async def send_members_list(ctx):
    members = ctx.channel.members
    async with ctx.channel.typing():
        for i in range (0, len(members)):
            await ctx.channel.send(members[i].mention)

@bot.command(name = 'admins')
async def send_admins_list(ctx):
    for i in range (0, len(ctx.channel.members)):
        if (ctx.channel.permissions_for(ctx.channel.members[i]).administrator):
            await ctx.channel.send(ctx.channel.members[i].mention)

@bot.command(name = 'ban')
@has_permissions(ban_members = True)
async def ban_member(ctx, target : discord.Member, *, reason = None):
    if (ctx.channel.permissions_for(target).administrator):
        await ctx.channel.send("Sorry, " + target.mention + " is an Admin")
    else:
        try:
            await target.ban(reason = reason)
            await ctx.channel.send("Banned" + target.mention)
        
        except:
            await ctx.channel.send("Something went wrong")

@ban_member.error
async def ban_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You do not have permissions to ban members")
    elif isinstance(error, BadArgument):
        await ctx.channel.send("Could not identify target")
    else:
        raise error

@bot.command(name = 'kick')
@has_permissions(kick_members = True)
async def kick_member(ctx, target : discord.Member, *, reason = None):
    if (ctx.channel.permissions_for(target).administrator):
        await ctx.channel.send("Sorry, " + target.mention + " is an Admin")
    else:
        try:
            await target.ban(reason = reason)
            await ctx.channel.send("Kicked " + target.mention)
        
        except:
            await ctx.channel.send("Something went wrong")

@kick_member.error
async def kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You do not have permissions to kick members")
    elif isinstance(error, BadArgument):
        await ctx.channel.send("Could not identify target")
    else:
        raise error

@bot.event
async def on_message(message):
    
    if ((message.content.lower().startswith('hi') or message.content.lower().startswith('hey') or message.content.lower().startswith('sup')) and message.author != bot.user) :
        await message.channel.send("Wassup " + message.author.mention)   # never directly do message.channel.send() as it will go to infinity loop
    
    elif (message.content.lower().startswith('gn')):
        await message.channel.send("Good Night " + message.author.mention)
    
    elif (message.content.lower().startswith('ok boomer')):
        await message.channel.send(file = discord.File('res/ok_boomer.jpg'))
        print(message.author.id)
    await bot.process_commands(message)

bot.run(tokens[2])
#nothing will run after this command ;)

# TODO : members in grp : member_count
# TODO : set_permissions()