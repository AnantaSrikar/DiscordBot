import discord 
from discord.ext import commands
from asyncio import sleep

class ownerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command('logout')
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.channel.send("Initiating logout")
        await self.bot.change_presence(status = discord.Status.offline)
        await sleep(1)
        await self.bot.logout()
        print("Logged out successfully")

def setup(bot):
    bot.add_cog(ownerCog(bot))