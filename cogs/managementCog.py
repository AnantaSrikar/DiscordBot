import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument

class mgmtCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'members')
    async def send_members_list(self, ctx):
        members = ctx.channel.members
        memberText = 'There are {} members in {}.\nThey are :\n'.format(len(members), ctx.guild.name)
        async with ctx.channel.typing():
            for i in range (0, len(members)):
                memberText += members[i].mention + '\n'
            await ctx.channel.send(memberText)

    @commands.command(name = 'admins')
    async def send_admins_list(self, ctx):
        async with ctx.channel.typing():
            adminsText = 'The admins of {} are :\n'.format(ctx.guild.name)
            for i in range (0, len(ctx.channel.members)):
                if (ctx.channel.permissions_for(ctx.channel.members[i]).administrator):
                    adminsText += ctx.channel.members[i].mention + '\n'
            await ctx.channel.send(adminsText)

    @commands.command(name = 'ban')
    @has_permissions(ban_members = True)
    async def ban_member(self, ctx, target : discord.Member, *, reason = None):
        if (ctx.channel.permissions_for(target).administrator):
            await ctx.channel.send("Sorry, {} is an Admin".format(target.mention))
        else:
            try:
                await target.ban(reason = reason)
                await ctx.channel.send("Banned {}".format(target.mention))
        
            except:
                await ctx.channel.send("Something went wrong")

    @ban_member.error
    async def ban_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.channel.send("You do not have permissions to ban members")
        elif isinstance(error, BadArgument):
            await ctx.channel.send("Could not identify target")
        else:
            raise error

    @commands.command(name = 'kick')
    @has_permissions(kick_members = True)
    async def kick_member(self, ctx, target : discord.Member, *, reason = None):
        if (ctx.channel.permissions_for(target).administrator):
            await ctx.channel.send("Sorry, {} is an Admin".format(target.mention) )
        else:
            try:
                await target.ban(reason = reason)
                await ctx.channel.send("Banned {}".format(target.mention) )
        
            except:
                await ctx.channel.send("Something went wrong")

    @kick_member.error
    async def kick_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.channel.send("You do not have permissions to kick members")
        elif isinstance(error, BadArgument):
            await ctx.channel.send("Could not identify target")
        else:
            raise error

def setup(bot):
    bot.add_cog(mgmtCog(bot))

async def getOwnerInfo(bot):
    if(not hasattr(bot, 'appInfo')):
        bot.appInfo = await bot.application_info()
    print('got owner info : {}'.format(bot.appInfo.owner))
    return  bot.appInfo.owner