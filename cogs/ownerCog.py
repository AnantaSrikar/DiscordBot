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

    @commands.command('invisible')
    @commands.is_owner()
    async def go_offline(self, ctx):
        await ctx.channel.send("Going invisible")
        await self.bot.change_presence(status = discord.Status.offline)
        print("Gone invisible")
    
    @go_offline.error
    async def offline_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send("You are not the owner of the bot. Only owners can use this command. To find out my owner, use `>owner`")

    @commands.command('visible')
    @commands.is_owner()
    async def come_visible(self, ctx):
        await ctx.channel.send("Coming back right away")
        await self.bot.change_presence(status = discord.Status.online)

    @come_visible.error
    async def online_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send("You are not the owner of the bot. Only owners can use this command. To find out my owner, use `>owner`")

def setup(bot):
    bot.add_cog(ownerCog(bot))