import discord 
from discord.ext import commands

class covCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('covid')
    async def tester(self, ctx):
        await ctx.channel.send('Stay tuned {}! COVID-19 update feature coming up soon.'.format(ctx.message.author.mention))

def setup(bot):
    bot.add_cog(covCog(bot))