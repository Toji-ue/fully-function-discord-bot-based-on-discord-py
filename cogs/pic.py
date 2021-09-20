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
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=neko&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    
    @commands.command(invoke_without_command=True,name="pedo", aliases=['kitsune'])
    async def h(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=kitsune&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
        


        
def setup(bot):
    bot.add_cog(PedoCog(bot))