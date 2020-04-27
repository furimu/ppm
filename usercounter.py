from discord.ext import commands

class User_Count(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.Cog.lstener()
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
    await ctx.send(f'現在までに{member.name}がvcに入った時間は`{uc[str(member.id)]["alcommand_Cog