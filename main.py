from discord.ext import commands
from datetime import datetime
import discord
import botinfo
import json
import traceback
bot = commands.Bot(command_prefix="p:")

cogs = [
    'admin',
    'mj'
]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except commands.ExtensionAlreadyLoaded:
        pass
 
    except Exception:    print(traceback.format_exc())


@bot.event
async def on_ready():
    print("yes")

bot.run(botinfo.token)