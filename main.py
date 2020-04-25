from discord.ext import commands
from datetime import datetime

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
async on_voice_state_update(member, before, after):
    dt_now = datetime.datetime.now()
    if str(member.id) not in uc.keys():
            uc[str(member.id)]= {}

    if before.channel is None:
        uc[str(member.id)]["start"] = str(dt_now.second)
        save(uc, user_count)

    if after.channel is None:
       uc[str(member.id)]["end"] = str(dt_now.second)   
       all = int(uc[str(member.id)]["end"]) - int(uc[str(member.id)]["start"])
       uc[str(member.id)]["all"] = str(all)
       save(uc, user_count)


       
       