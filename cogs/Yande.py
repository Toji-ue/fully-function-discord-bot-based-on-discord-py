import discord
from discord import channel
from discord.ext import commands
from requests import get
import aiohttp
import json
import requests
from yarl import URL

class yandeCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True,aliases=['suisei'])
    async def sussei(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Hoshimachi_Suisei+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,name="simp", aliases=['hololive'])
    async def h(self,ctx):
       async with aiohttp.ClientSession() as session:
          apicall = "https://yande.re/post.json?limit=1&tags=Hololive+order%3ARandom"
          response = requests.get(apicall)
          response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['sora'])
    async def sky(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Tokino_Sora+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['roboco'])
    async def robo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=roboco-san+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['fubuki'])
    async def fk(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Shirakami_Fubuki+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aki'])
    async def ak(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Aki_Rosenthal+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['matsuri'])
    async def mat(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Natsuiro_Matsuri+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['miko'])
    async def fakkyu(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Sakura_Miko+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aqua'])
    async def akua(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Minato_Aqua+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['shion'])
    async def garlic(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Murasaki_Shion+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['ayame'])
    async def yodayo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Nakiri_Ayame+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['choco'])
    async def sensei(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Yuzuki_Choco+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['subaru'])
    async def duck(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Oozora_Subaru+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['AZKi'])
    async def azk(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=azki+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['mio'])
    async def mama(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Ookami_Mio+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['okayu'])
    async def lazy_cat(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Nekomata_Okayu+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['korone'])
    async def doog(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Inugami_Korone+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['pekora'])
    async def warcrime(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Usada_Pekora+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['rushia'])
    async def rushie1(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Uruha_Rushia+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['marine'])
    async def hornie(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Houshou_Marine+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['flare'])
    async def fla(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Shiranui_Flare+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['noel'])
    async def booba(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Shirogane_Noel+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['coco'])
    async def cocomelon(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Kiryu_Coco+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['kanata'])
    async def gorilla(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Amane_Kanata+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['watame'])
    async def wataoji(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Tsunomaki_Watame+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['towa'])
    async def angel(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Tokoyami_Towa+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['luna'])
    async def nanora(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Himemori_Luna+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['lamy'])
    async def mom(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Yukihana_Lamy+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['nene'])
    async def momo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Momosuzu_Nene+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['botan'])
    async def fpslion(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Shishiro_Botan+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['polka'])
    async def pol(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Omaru_Polka+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aloe'])
    async def rip(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Mano_Aloe+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['risu'])
    async def ayunda(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Ayunda_Risu+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['Haachama'])
    async def akai(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://yande.re/post.json?limit=1&tags=Akai_Haato+order%3ARandom"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
def setup(bot):
    bot.add_cog(yandeCog(bot))