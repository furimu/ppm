from discord.ext import commands
import discord, emb, traceback

class MJ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="チーム分け")
    async def team_sprit(self, ctx, role:discord.Role, limit:int):
        """役職でチームをわけます"""
        d={}
        c=1
        
        for member in role.members:
            if str(c) not in d.keys():
                d[str(c)] = []
           
            d[str(c)].append(str(member.id))
 
            if len(d[str(c)]) > limit:
                c += 1
                continue
            elif len(d[str(c)]) == limit:

                e = emb.ma(title=f"{c}番のチーム", desc=",".join(ctx.guild.get_member(int(m)).mention for m in d[str(c)]))
                await ctx.send(embed=e)

            elif len(d[str(c)]) < limit:
                e = emb.ma(title=f"{c}番のチーム", desc=",".join(ctx.guild.get_member(int(m)).mention for m in d[str(c)]))
                await ctx.send(embed=e)
    @team_sprit.error
    async def team_error(self, ctx, error):
        await ctx.send(f'```py\n{traceback.format_exc()}\n```')
           

def setup(bot):
    bot.add_cog(MJ(bot))