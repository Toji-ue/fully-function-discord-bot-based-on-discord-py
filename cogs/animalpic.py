# -*- coding: utf-8 -*-
import discord
from discord import channel
from discord.ext import commands
from requests import get
import aiohttp
import json
import requests
from yarl import URL
class animalCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True,aliases=['doggo'])
    async def dog(self,ctx):
      async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/img/dog') 
         dogjson = await request.json()
      embed = discord.Embed(title="Cute Doggo!", color=discord.Color.gold()) 
      embed.set_image(url=dogjson['link']) 
      await ctx.send(embed=embed)
    @commands.command(invoke_without_command=True,aliases=['catto'])
    async def cat(self,ctx):
       async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/cat')
          catjson = await request.json()
       embed = discord.Embed(title="Catto（Φ ω Φ）", color=discord.Color.gold())
       embed.set_image(url=catjson['link'])
       await ctx.send(embed=embed)
    @commands.command(invoke_without_command=True,aliases=['pat'])
    async def patpat(self,ctx):
      async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/animu/pat') 
         patjson = await request.json()
      embed = discord.Embed(title="PAT", color=discord.Color.blurple()) 
      embed.set_image(url=patjson['link']) 
      await ctx.send(embed=embed,delete_after=20.0)
    @commands.command(invoke_without_command=True,aliases=['wink'])
    async def win(self,ctx):
      async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/animu/wink') 
         winkjson = await request.json()
      embed = discord.Embed(title="wink wink", color=discord.Color.blurple()) 
      embed.set_image(url=winkjson['link']) 
      await ctx.send(embed=embed,delete_after=20.0)
    @commands.command(invoke_without_command=True,aliases=['hug'])
    async def huggu(self,ctx):
      async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/animu/hug') 
         hugjson = await request.json()
      embed = discord.Embed(title="hug", color=discord.Color.blurple()) 
      embed.set_image(url=hugjson['link']) 
      await ctx.send(embed=embed,delete_after=20.0)

def setup(bot):
    bot.add_cog(animalCog(bot))


