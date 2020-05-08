from discord.ext import commands, tasks
import os
import subprocess
import traceback

 
 
 
class Admin(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot
 
 
    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)
 
 
    @commands.command()
    async def discord_py(self, ctx):
        await ctx.send(discord.__version__)
 
    @commands.command()
    async def load(self, ctx, module:str, opt:str = None):
        if opt is None:
            self.bot.load_extension(module)
 
        elif opt == 'un':
            self.bot.unload_extension(module)
 
        elif opt == 're':
            self.bot.reload_extension(module)
 
        else:
            return await ctx.message.add_reaction('\N{BLACK QUESTION MARK ORNAMENT}')
        
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
 
    @load.error
    async def load_error(self, ctx, error):
        try:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        except:
            print(traceback.format_exc())

def setup(bot):
    bot.add_cog(Admin(bot))