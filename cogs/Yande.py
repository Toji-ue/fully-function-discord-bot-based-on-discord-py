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
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Hoshimachi_Suisei&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,name="simp", aliases=['hololive'])
    async def h(self,ctx):
       async with aiohttp.ClientSession() as session:
          apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Hololive&nsfw=none&random=true&rating%3A"
          response = requests.get(apicall)
          response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['sora'])
    async def sky(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Tokino_Sora&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'],delete_after=30.0)
    @commands.command(invoke_without_command=True,aliases=['roboco'])
    async def robo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=roboco-san&nsfw=none%&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['fubuki'])
    async def fk(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Shirakami_Fubuki&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aki'])
    async def ak(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Aki_Rosenthal&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['matsuri'])
    async def mat(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Natsuiro_Matsuri&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['miko'])
    async def fakkyu(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Sakura_Miko&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aqua'])
    async def akua(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Minato_Aqua&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['shion'])
    async def garlic(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Murasaki_Shion&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['ayame'])
    async def yodayo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Nakiri_Ayame&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['choco'])
    async def sensei(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Yuzuki_Choco&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['subaru'])
    async def duck(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Oozora_Subaru&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['AZKi'])
    async def azk(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=azki&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['mio'])
    async def mama(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Ookami_Mio&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['okayu'])
    async def lazy_cat(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Nekomata_Okayu&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['korone'])
    async def doog(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Inugami_Korone&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['pekora'])
    async def warcrime(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Usada_Pekora&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['rushia'])
    async def rushie1(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Uruha_Rushia&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['marine'])
    async def hornie(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Houshou_Marine&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['flare'])
    async def fla(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Shiranui_Flare&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['noel'])
    async def booba(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Shirogane_Noel&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['coco'])
    async def cocomelon(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Kiryu_Coco&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['kanata'])
    async def gorilla(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Amane_Kanata&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['watame'])
    async def wataoji(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Tsunomaki_Watame&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['towa'])
    async def angel(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Tokoyaki_Towa&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['luna'])
    async def nanora(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Himemori_Luna&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['lamy'])
    async def mom(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Yukihana_Lamy&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['nene'])
    async def momo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Momosuzu_Nene&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['botan'])
    async def fpslion(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Shishiro_Botan&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['polka'])
    async def pol(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Omaru_Polka&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['aloe'])
    async def rip(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Mano_Aloe&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['risu'])
    async def ayunda(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Ayunda_Risu&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['Haachama'])
    async def akai(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Akai_Haato&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['moona'])
    async def mooon(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Moona_Hoshinova&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['iofi'])
    async def lofi(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Airani_Iofi&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['ollie'])
    async def zom(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Kureiji_Ollie&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['anya'])
    async def an(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Anya_Melfissa&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['reine'])
    async def milf(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Pavolia_Reine&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['calli'])
    async def papa(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Mori_Calliope&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['kiara'])
    async def chicken(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Takashina_Kiara&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['ina'])
    async def inaugh(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Ninomae_Ina'nis&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['gura'])
    async def shark(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Gawr_Gura&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['amelia'])
    async def ZA_WARUDO(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Watson_Amelia&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['irys'])
    async def hope(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=irys_%28hololive%29&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['sana'])
    async def big(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Tsukumo_Sana&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['fauna'])
    async def ceres(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Ceres_Fauna&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['kronii'])
    async def under_booba(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Ouro_Kronii&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['mumei'])
    async def forgor(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Nanashi_Mumei&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['baelz'])
    async def mause(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Hakos_Baelz&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['yogiri'])
    async def dunno(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=yogiri_%28hololive%29&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['civia'])
    async def unicorn(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=civia&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['echo'])
    async def spade(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=Spade_Echo&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['doris'])
    async def nemo(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=doris_%28hololive%29&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['rosalyn'])
    async def rose(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=rosalyn_%28hololive%29&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['artia'])
    async def art(self,ctx):
       async with aiohttp.ClientSession() as session:
           apicall = "https://danbooru.donmai.us/posts.json?limit=1&tags=artia&nsfw=none&random=true&rating%3A"
           response = requests.get(apicall)
           response = response.json()
       for r in response:
          await ctx.send(r['file_url'])
    @commands.command(invoke_without_command=True,aliases=['chris'])
    async def hitomi(self,ctx):
        await ctx.send('Ò̶̢̜̗̙̮̅͗̾ȉ̸̠͎̯̥̱́́ ̷͈̰̠̝̥̑̀͌̚͝L̶͍̬̎͋̂̋́ổ̴̢̝̭̖́o̸̠͕̮̒̈́͑̂ͅk̵̨̧̥̙̯̆̉͑͠s̴̬͖̖̄ ̵̝̼̱̈L̷̨͆̄͌͝i̴̤̳̜͕̾͝ͅk̵̬̹̣̦͕͐̊e̶͔̫̹͑ ̷̢̧͈̂̽̅̋́Y̵͔̯̭͌̇o̸̦͈̯̰͂̉ȗ̵̜̝̮̼͔̒̍̕̕ ̴̦̻͔͂̄̎̓Ḫ̸̠͍͛á̴̞̬̽̿͒͋v̸̝͎͊͘e̷̫͈̮̝͐́͋̍͝ ̴̺̙̗̩̮͛R̷̳̻̱͔̣̒̀̎̎͘e̵͍͕̲̒͑ã̸̛̱̺͇̊́͝c̸͖̰͕͙͊́ͅḩ̸̞̲͇̋͠͝e̵̫̬͑d̴̯̳̱͕̋̌͂̐͝ ̵̣̣̮͉̮͗̔̔̚Ť̸̡̧̥̤̍̈́̉h̵̢͎̫͎̿͘ȅ̷̘ ̴̛̻̠͒̄F̵̦͉̯́́͐́̚o̸̡̨̱̒͆̈́r̴̙͍̤̈ḇ̴̟̑ȉ̵̻̲͔d̵͕̥͇̘͋̂̔̓͝ḋ̶̨̬̯̆e̴͚͎̠͚̼̍̓͆n̵̛̥͝ ̶̧͖͈̹̋͐̑K̵̹̾̀ņ̸̡͙̮̥̆̽͊o̵̲͍̹̞̾́̕ŵ̶̜̓l̵͈̱̈͆e̶͖̝̯͑̇̐͋̕ͅd̶̛̝̻̼̩͍͊̑͑̚g̸̖͍̝͐͘e̶̳̒̍̑̃')
    
def setup(bot):
    bot.add_cog(yandeCog(bot))