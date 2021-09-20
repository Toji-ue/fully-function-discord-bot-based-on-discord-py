import discord
from discord.ext import commands
import json
from requests import get
from discord import channel
import akaneko
import aiohttp
import requests
from requests.sessions import session
from yarl import URL

class PedoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True,name="pedo gaming", aliases=['neko'])
    async def shibe(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=neko+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'],delete_after=10.0)
    
    @commands.command(invoke_without_command=True,name="pedo", aliases=['kitsune'])
    async def h(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=kitsune+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'],delete_after=10.0)
        


        
def setup(bot):
    bot.add_cog(PedoCog(bot))