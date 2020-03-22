import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument

class mgmtCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name = 'members')
	async def send_members_list(self, ctx):
		members = ctx.channel.members
		bots = []
		for member in members:
			if(member.bot):
				bots.append(member)
				members.remove(member)

		memberText = 'There are {} members and {} bots in {}.\nThe members are :\n'.format(len(members), len(bots), ctx.guild.name)
		
		for member in members:
			memberText += member.mention + '\n'        
		
		memberText += '\nThe bots are :\n'
		
		for bot in bots:
			memberText += bot.mention + '\n'

		async with ctx.channel.typing():
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
				await ctx.channel.send("Banned {}".format(target.mention))
				await target.ban(reason = reason)
		
			except:
				await ctx.channel.send("Something went wrong")

	@ban_member.error
	async def ban_error(self, ctx, error):
		if isinstance(error, CheckFailure):
			await ctx.channel.send("You do not have permissions to ban members")
		elif isinstance(error, BadArgument):
			await ctx.channel.send("Could not identify member")
		else:
			raise error

	@commands.command(name = 'kick')
	@has_permissions(kick_members = True)
	async def kick_member(self, ctx, target : discord.Member, *, reason = None):
		if (ctx.channel.permissions_for(target).administrator):
			await ctx.channel.send("Sorry, {} is an Admin".format(target.mention) )
		else:
			try:
				await ctx.channel.send("Kicked {}".format(target.mention))
				await target.kick(reason = reason)
		
			except:
				await ctx.channel.send("Something went wrong")

	@kick_member.error
	async def kick_error(self, ctx, error):
		if isinstance(error, CheckFailure):
			await ctx.channel.send("You do not have permissions to kick members")
		elif isinstance(error, BadArgument):
			await ctx.channel.send("Could not identify member")
		else:
			raise error
		
	@commands.command(name = 'mute')
	@has_permissions(administrator = True)
	async def mute_user(self, ctx, member : discord.Member):
		role = discord.utils.get(ctx.guild.roles, name = "Muted")
		if(role == None):
			await ctx.channel.send('I have to be updated to make a muted role')
		else:
			await member.add_roles(role)
			await ctx.channel.send('Muted {}'.format(member.mention))

	@mute_user.error
	async def mute_errors(self, ctx, error):
		if isinstance(error, CheckFailure):
			await ctx.channel.send('You do not have the permission to mute members')
		elif isinstance(error, BadArgument):
			await ctx.channel.send("Coudn't identify member")

def setup(bot):
	bot.add_cog(mgmtCog(bot))