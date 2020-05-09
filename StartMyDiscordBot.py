# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:44:55 2019

@author: ANANTA SRIKAR
"""

from discord.ext.commands import Bot
import os
from utils.generalFuncs import tokens

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Making the file work from anywhere

bot = Bot(command_prefix='>')
bot.remove_command("help")

bot.load_extension('cogs.testCog')
bot.load_extension('cogs.managementCog')
bot.load_extension('cogs.ownerCog')
bot.load_extension('cogs.covCog')
bot.load_extension('cogs.generalCog')
bot.load_extension('cogs.eventsCog')

bot.run(tokens()["bot_token"])
#nothing will run after this command ;)

# TODO : set_permissions() if command is sent by admin
# TODO : add unban
# TODO : add timed messages when nobody is chatting
# TODO : Fix bug when someone says yeah
# TODO : mute members on a channel
# TODO : command to unsubscribe from xkcd