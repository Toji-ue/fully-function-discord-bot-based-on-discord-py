# -*- coding: utf-8 -*-
import discord
from discord import client
from discord.ext import commands
import sys, traceback

from discord.ext.commands import bot

def get_prefix(bot, message):
    prefixes = ['>?', '.', '!?']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.ui',
                      'cogs.translator',
                      'cogs.meme',
                      'cogs.music',
                      'cogs.pic',
                      'cogs.wiki',
                      'cogs.8ball',
                      'cogs.van_mau',
                      'cogs.help',
                      'cogs.animalpic',
                      'cogs.Yande']

bot = commands.Bot(command_prefix=get_prefix, description='lol', help_command=None)
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(activity=discord.Game(name="mẹ mày"))
    print(f'Successfully logged in and booted...!')
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! ping của bot là {0} ms'.format(round(bot.latency, 1)),delete_after=20.0)
@bot.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

bot.run('token', bot=True, reconnect=True)
