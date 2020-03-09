import discord 
from discord.ext import commands
import cogs.coronaInfo

class covCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('covid')
    async def tester(self, ctx):
        #await ctx.channel.send('Stay tuned {}! COVID-19 update feature coming up soon.'.format(ctx.message.author.mention))
        await ctx.channel.send(coronaInfo.getInfo())

def setup(bot):
    bot.add_cog(covCog(bot))