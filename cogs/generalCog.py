import discord 
from discord.ext import commands
from random import shuffle, randint
from asyncio import sleep
from utils.generalFuncs import return_weather, NewsFromBBC, indianNews

class generalCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'start')
	async def ping(self, ctx):
		await ctx.channel.send("Hey {} . I'm still awake btw....".format(ctx.message.author.mention))

	@commands.command(name = 'help')
	async def helpHim(self, ctx):
		async with ctx.channel.typing():
			fileManager = open('res/bot_intro.txt', 'r')
			bot_intro = fileManager.read()
			bot_intro = bot_intro.replace('Srikar', self.bot.appInfo.owner.mention)
			fileManager.close()
			await ctx.channel.send(bot_intro)

	@commands.command(name = 'weatherUpdate')
	async def send_weather(self, ctx):
		city = ctx.message.content[15:]
		await ctx.channel.send(return_weather(city))

	@commands.command(name = 'intNews')
	async def send_int_news(self, ctx):
		async with ctx.channel.typing():
			await ctx.channel.send(NewsFromBBC())

	@commands.command(name = 'indNews')
	async def send_ind_news(self, ctx):
		async with ctx.channel.typing():
			await ctx.channel.send(indianNews())

	@commands.command(name = 'startxkcd')  # Thanks Raghav. Asyncio is the best indeed. So is XKCD
	async def startXKCD(self, ctx):
		await ctx.channel.send("XKCD hourly service coming up")
		l = [i for i in range(1, 2300, 1)]
		shuffle(l)
		while(len(l) > 0):
			index = randint(0, len(l))
			number = l[index]
			l.pop(index)
			url = "https://xkcd.com/" + str(number)
			await ctx.channel.send("@everyone here's you xkcd for the hour : " + url)
			await sleep(60 * 60)

	@commands.command(name = 'owner')
	async def send_owner(self, ctx):
		await ctx.channel.send('{} owns me. Literally!'.format(self.bot.appInfo.owner.mention))

	@commands.command()
	async def send_message(self, ctx, *, message : str):
		await ctx.channel.send(message)

def setup(bot):
	bot.add_cog(generalCog(bot))