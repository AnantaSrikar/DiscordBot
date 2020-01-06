# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:44:55 2019

@author: ANANTA SRIKAR
"""
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument, CommandNotFound
import requests

tokens = []

owner_id = 605674719731253263
owner = discord.user.User

def getTokens():
    fileManager = open('res/TOKENS.txt', 'r')  #make the file in such a way that token[0] is for news, token[1] for weather, token[2] for bot
    tokenText = fileManager.read()
    global tokens
    tokens = tokenText.split('\n')

def NewsFromBBC(): 

    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={}".format(tokens[0])
 
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
    
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(tokens[0])

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
maker_mention = tokens[3]  #for mentioning ones own self, get the mention sting. Ex : <@605674719731253263>

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
    await ctx.channel.send("Hey " + ctx.message.author.mention + ". I'm still awake btw....")

@bot.command(name = 'help')
async def helpHim(ctx):
    async with ctx.channel.typing():
        fileManager = open('res/bot_intro.txt', 'r')
        bot_intro = fileManager.read()
        bot_intro = bot_intro.replace('Srikar', maker_mention)
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
    memberText = 'There are {} members in {}.\nThey are :\n'.format(len(members), ctx.guild.name)
    async with ctx.channel.typing():
        for i in range (0, len(members)):
            memberText += members[i].mention + '\n'
        await ctx.channel.send(memberText)

@bot.command(name = 'admins')
async def send_admins_list(ctx):
    async with ctx.channel.typing():
        adminsText = 'The admins of {} are :\n'.format(ctx.guild.name)
        for i in range (0, len(ctx.channel.members)):
            if (ctx.channel.permissions_for(ctx.channel.members[i]).administrator):
                adminsText += ctx.channel.members[i].mention + '\n'
        await ctx.channel.send(adminsText)

@bot.command(name = 'owner')
async def send_owner(ctx):
    await ctx.channel.send('{} owns me. Literally!'.format(owner.mention))

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
    
    elif ((message.content.lower().startswith('gn') or 'good night' in message.content.lower()) and message.author != bot.user):
        await message.channel.send("Good Night " + message.author.mention)
    
    elif (message.content.lower().startswith('ok boomer')):
        await message.channel.send(file = discord.File('res/ok_boomer.jpg'))

    elif ('bot' in message.content.lower() and message.author != bot.user):
        await message.channel.send("Hey {}! U wanna talk to me?".format(message.author.mention))
    
    elif ('bye' in message.content.lower() and message.author != bot.user):
        await message.channel.send('Goodbye {}'.format(message.author.mention))

    if(message.author == owner):
        #print('My owner has sen a message!') ---> do something which owner only has access to
        pass # don't forget to remove this after adding a function
    
    await bot.process_commands(message)

@bot.event
async def on_member_remove(member):
    await member.guild.system_channel.send("{} has left {}".format(member.mention, member.guild.name))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send("Sorry " + ctx.message.author.mention + "! I still don't know that command 😞\nTry `>help` to see what I can do.")

bot.run(tokens[2])
#nothing will run after this command ;)

# TODO : set_permissions()
#TODO : add timed messages when nobody is chatting