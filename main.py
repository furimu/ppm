from discord.ext import commands

bot = commands.Bot(command_prefix="p:")



@bot.event
async def on_ready():
    print("yes")

@bot.event
async on_voice_state_update(member, before, after):
    if after.channel is None:
        