from discord.ext import commands
from datetime import datetime
import discord
import botinfo
import json
bot = commands.Bot(command_prefix="p:")

cogs = [
    'usercount'
]

send_error_channel = bot.get_channel(663772130978168842)
        await send_error_channel.send('新規エラー')
        for cog in cogs:
            try:
                bot.load_extension(cog)
            except commands.ExtensionAlreadyLoaded:
                pass
 
            except Exception:
                await send_error_channel.send(f'```py\n{traceback.format_exc()}\n```')


@bot.event
async def on_ready():
    print("yes")

bot.run(botinfo.token)