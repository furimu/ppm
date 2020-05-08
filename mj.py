from discord.ext import commands
import discord, emb

class MJ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="チーム分け")
    async def team_sprit(self, ctx, role:discord.Role, limit:int):
        """役職でチームをわけます"""
        d={}
        c=1
        
        for member in role.members:
            if c not in d.keys():
                d[str(c)] = []

            print(str(member))
           

            d[str(c)].append(str(member.id))
            if len(d[str(c)]) < limit:
                c += 1
                continue
            elif len(d[str(c)]) == limit:
                e = emb(title=f"{c}番のチーム", desc=",".join(ctx.guild.get_member(int(m).mention for m in d[str(c)])))
                await ctx.send(embed=e)

           

def setup(bot):
    bot.add_cog(MJ(bot))