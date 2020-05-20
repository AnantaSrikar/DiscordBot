import discord 
from discord.ext import commands

class messageHandler(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command('join_voice')
	async def join_voice(self, ctx):
		print('Got the command')
		try:
			print('In the try')
			voice_channel = ctx.author.voice.channel

			try:
				await voice_channel.connect()
				await ctx.channel.send('Joined voice channel {}!'.format(voice_channel))
			except Exception as e:
				print('Failed to join voice channel, Exception : {}'.format(e))

		except:
			await ctx.channel.send('You should be in a voice channel first {}!'.format(ctx.author.mention))
	

	@commands.command('test_voice')
	async def test_voice(self, ctx):
		try:
			source = await discord.FFmpegOpusAudio.from_probe("res/Faded.mp3")
			await ctx.voice_client.play(source)
			await ctx.channel.send('Playing song now')
		except Exception as e:
			print("Error occured. Exception : {}".format(e))
	
	
	@commands.command('leave_voice')
	async def leave_voice(self, ctx):
		await ctx.voice_client.disconnect()

def setup(bot):
	bot.add_cog(messageHandler(bot))


# TODO : voice_client.is_connected()