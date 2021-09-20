from typing import ContextManager, Text
import googletrans
from googletrans import Translator
import discord
from discord.ext import commands
import json
class translatorCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command=True,name="translator", aliases=['ts','TS','Ts','translate'])   
    async def translate(self,ctx, lang, *, thing):
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        await ctx.send(translation.text)
    

def setup(bot):
    bot.add_cog(translatorCog(bot))
        


