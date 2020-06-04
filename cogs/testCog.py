import discord 
from discord.ext import commands

class messageHandler(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command('test_cog')
	async def tester(self, ctx):
		print("In the command")
		await ctx.channel.send('Good news {}! Cogs are working just fine'.format(ctx.message.author.mention))

def setup(bot):
	bot.add_cog(messageHandler(bot))