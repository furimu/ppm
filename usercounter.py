from discord.ext import commands
from datetime import datetime
import json
import discord
 
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
al = load("all")


class User_Counter(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        dt_now = datetime.now()
        if str(member.id) not in uc.keys():
            uc[str(member.id)]= {}
 
        if before.channel is None:
            uc[str(member.id)]["starthours"] = str(dt_now.hour)
            uc[str(member.id)]["startminutes"] = str(dt_now.minute)

            uc[str(member.id)]["startsecond"] = str(dt_now.second)

            save(uc, "user_count")
 
        if after.channel is None:
           uc[str(member.id)]["endhours"] = str(dt_now.hour)
           uc[str(member.id)]["endminutes"] = str(dt_now.minute)

           uc[str(member.id)]["endsecond"] = str(dt_now.second)   
           save(uc, "user_count")
             

         

           uc[str(member.id)]["all"] = str(all)
           save(uc, "user_count")
 
 
    @commands.command()
    async def show(self, ctx):
        member = ctx.author
        if str(member.id) not in uc.keys():
            return await ctx.send('貴方がvcに入ったデータはありません')
 
        elif 'all' not in uc[str(member.id)].keys():
            return await ctx.send('貴方がvcに入った合計時間のデータはありません')
        await ctx.send(f'現在までに貴方がvcに入った時間は`{uc[str(member.id)]["all"]}秒`です')
 
 
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def adshow(self, ctx, member: discord.Member):
        if str(member.id) not in uc.keys():
            return await ctx.send(f'{member.name}がvcに入ったデータはありません')
 
        elif 'all' not in uc[str(member.id)].keys():
            return await ctx.send(f'{member.name}がvcに入った合計時間のデータはありません')
        await ctx.send(f'現在までに{member.name}がvcに入った時間は`{uc[str(member.id)]["all"]}秒`です')

    @commands.command()
    async def top_(self, ctx,limit: int):
        mem = {}
        for member in ctx.guild.members:
            if str(member.id) not in uc.keys():
                continue
            for k, v in uc[str(member.id)].items():
                if k != 'all':
                    continue
                mem[str(member.id)] = str(uc[str(member.id)]["all"])

            else:
                continue

        result= sorted(mem, reverse=True)
        e = discord.Embed(
            title = f"**Top{limit}**")
        count = 0


        for r in sorted(result, reverse=True):
            for l in range(limit):
           
                m = ctx.guild.get_member(int(r))
                count = count +1
                e.add_field( 
                    name= f"{count}: {str(m)}",
                    value = str(uc[r]["all"]),
                    inline=True)
      

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(User_Counter(bot))