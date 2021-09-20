import discord
from discord.ext import commands
from requests import get
import json

class memeCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True, aliases=['meme','m'])
    async def mimi(ctx,msg):
     content = get("https://meme-api.herokuapp.com/gimme").text
     data = json.loads(content,)
     meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
     await msg.reply(embed=meme)

def setup(bot):
    bot.add_cog(memeCog(bot))
