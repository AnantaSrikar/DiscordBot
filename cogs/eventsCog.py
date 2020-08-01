from discord.ext import commands
from discord import File
from discord.ext.commands import CommandNotFound

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):  
		print("\nLogged in as: " + str(self.bot.user))
		print("------------------")

		if(not hasattr(self.bot, 'appInfo')):
			self.bot.appInfo = await self.bot.application_info()

	@commands.Cog.listener()
	async def on_message(self, message):

		msg = message.content.lower()

		# For the opponent, XD bot

		if (message.author.name == 'xD'):
			await message.channel.send("{} you are so dead XD".format(message.author.mention))

		if(message.author != self.bot.user and not(message.author.bot)):

			if ((msg.startswith('hi') or msg.startswith('hey') or msg.startswith('sup'))) :
				await message.channel.send("Wassup {}".format(message.author.mention))   # never directly do message.channel.send() as it will go to infinity loop
			
			elif ((msg.startswith('gn') or 'good night' in msg)):
				await message.channel.send("Good Night {}".format(message.author.mention) )
			
			elif ('boomer' in msg):
				await message.channel.send(file = File('res/ok_boomer.jpg') )
			
			elif ('bye' in msg):
				await message.channel.send('Goodbye {}'.format(message.author.mention))

			if(message.author == self.bot.appInfo.owner):
				#print('My owner has sent a message!') ---> do something which owner only has access to
				pass # don't forget to remove this after adding a function

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		await member.guild.system_channel.send("{} has left {}".format(member.mention, member.guild.name)) # TODO : shows invalid-user when banned

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, CommandNotFound):
			await ctx.channel.send("Sorry {} ! I still don't know that command 😞\nTry `>help` to see what I can do.".format( ctx.message.author.mention))

def setup(bot):
	bot.add_cog(Events(bot))