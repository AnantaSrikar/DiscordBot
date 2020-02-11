import discord 
from discord.ext import commands

class ownerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('ownerCog')
    async def tester(self, ctx):
        print("In the command")
        await ctx.channel.send('Good news {}! Owner Cogs are working just fine'.format(ctx.message.author.mention))
    
    @commands.command('logout')
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.channel.send('Owner detected, will logout once feature is added')

def setup(bot):
    bot.add_cog(ownerCog(bot))