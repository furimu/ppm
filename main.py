from discord.ext import commands
from datetime import datetime
import discord
import botinfo
import json
bot = commands.Bot(command_prefix="p:")

DEFAULT_MESSAGE = {}

def save(value, module):
    with open(f'{module}.json', 'w', encoding= 'utf-8') as f:
        return json.dump(value, f, ensure_ascii=False, indent=4)


def load(module):
    try:
        with open(f'{module}.json', encoding='utf-8') as f:
            return json.load(f)

    except OSError:
        save(DEFAULT_MESSAGE, module)

uc= load("user_count")

@bot.event
async def on_ready():
    print("yes")

@bot.event
async def on_voice_state_update(member, before, after):
    dt_now = datetime.now()
    if str(member.id) not in uc.keys():
            uc[str(member.id)]= {}

    if before.channel is None:
        uc[str(member.id)]["start"] = str(dt_now.second)
        save(uc, "user_count")

    if after.channel is None:
       uc[str(member.id)]["end"] = str(dt_now.second)   
       if 'all' not in uc[str(member.id)].keys():
           all = int(uc[str(member.id)]["end"]) - int(uc[str(member.id)]["start"])
   
       else:
           all = int(uc[str(member.id)]["all"]) + (int(uc[str(member.id)]["end"]) - int(uc[str(member.id)]["start"]))
       print(all)
       uc[str(member.id)]["all"] = str(all)
       save(uc, "user_count")


@bot.command()
async def show(ctx):
    member = ctx.author
    if str(member.id) not in uc.keys():
        return await ctx.send('貴方がvcに入ったデータはありません')

    elif 'all' not in uc[str(member.id)].keys():
        return await ctx.send('貴方がvcに入った合計時間のデータはありません')
    await ctx.send(f'現在までに貴方がvcに入った時間は`{uc[str(member.id)]["all"]}秒`です')


@bot.command()
@commands.has_permissions(administrator = True)
async def adshow(ctx, member: discord.Member):
    if str(member.id) not in uc.keys():
        return await ctx.send(f'{member.name}がvcに入ったデータはありません')

    elif 'all' not in uc[str(member.id)].keys():
        return await ctx.send(f'{member.name}がvcに入った合計時間のデータはありません')
    await ctx.send(f'現在までに{member.name}がvcに入った時間は`{uc[str(member.id)]["all"]}秒`です')

@bot.command

bot.run(botinfo.token)