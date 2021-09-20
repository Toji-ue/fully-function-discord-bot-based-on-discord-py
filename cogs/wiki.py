import discord
from discord.ext import commands
import asyncio
import wikipedia
from random import randint

current_language = "en"

class wikiCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True, aliases=['wiki','wk'])
    async def search(self,ctx,arg):
        definition = wikipedia.summary(arg,sentences=3,chars=1000)
        embed = discord.Embed(title="***wiki:***",description=definition,color = discord.Color.random())
        await ctx.send(embed=embed)

        
def setup(bot):
    bot.add_cog(wikiCog(bot))