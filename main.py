from discord.ext import commands
from datetime import datetime
import discord
import botinfo
import json
bot = commands.Bot(command_prefix="p:")

cogs = [
    'usercount'
]

@bot.event
async def on_ready():
    print("yes")

bot.run(botinfo.token)