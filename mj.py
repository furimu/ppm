from discord.ext import commands
import discord, emb

class MJ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="チーム分け")
    async def team_sprit(self, ctx, role:discord.Role, limit:int)
        """役職でチームをわけます""
        d={}
        c=1
        e = 
        for member in role.members:
        if c not in d.keys():
            d[str(c)] = []

        if len(d[str(c)] == limit:
            c += 1
            continue

        