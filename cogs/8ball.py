import discord
from discord.ext import commands
import random

class eightballCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(invoke_without_command=True,aliases=['8ball','ball','8b'])
    async def b(self,ctx):
        responses = ['có cl',
                     'mơ à',
                      'ảo ma',
                      'làm j có',
                      'không.'
                      'h',
                      'có',
                      'bạn là nhất',
                      'nhất bạn',
                      'đồng ý']
        await ctx.send(random.choice(responses))
def setup(bot):
    bot.add_cog(eightballCog(bot))