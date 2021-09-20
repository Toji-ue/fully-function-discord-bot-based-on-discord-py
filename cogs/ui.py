import discord
from discord import colour
from discord import member
from discord import message
from discord.ext import commands
import datetime

class uiCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(invoke_without_command=True, aliases=['user', 'uinfo', 'info', 'ui'])
    async def userinfo(self,ctx,*,user: discord.Member = None):
        if user is None:
           member = ctx.author
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(0xff3400),
        title = f"{ctx.author}")
        date_format = "%a, %d %b %Y %I:%M %p"
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(0xff3400),
        title = f"{ctx.author}")
        embed.add_field(name="**•ID•**", value=f"{member.id}", inline=True)
        embed.add_field(name="**•Trạng Thái•**", value=str(member.status).replace("dnd", "Do Not Disturb"), inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"**•Roles• ({len(ctx.author.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name="**•Ngày Tạo Account•**", value=f"Account Creation:{member.created_at.strftime(date_format)}".replace("-", "/"), inline=True)
        embed.add_field(name="**•Join Server Vào Ngày•**", value=f"{member.joined_at.date()}".replace("-", "/"), inline = True)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed,delete_after=20.0)

     

def setup(bot):
    bot.add_cog(uiCog(bot))




