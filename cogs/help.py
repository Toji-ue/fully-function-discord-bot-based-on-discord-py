import discord
from discord import client
from discord.ext import commands
import datetime

from discord.ext.commands import bot
from discord.utils import get

class helpCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(invoke_without_commands=True,aliases=['h'])
    async def help(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = 'Các Câu Lệnh',
            description = '(っ˘ω˘ς )',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Amelia Little Note*',value='*Không Biết Lệnh Xài Như Nào Thì Gõ .help_<lệnh> nhé!*',inline=False)
        embed.add_field(name='*Prefixes*',value='*`.` `>?` `!?`*',inline=False)
        embed.add_field(name='Fun',value='`8ball` `meme` `vanmau` ',inline=False)
        embed.add_field(name='Music',value=' `play` `stop` `queue` `nowplaying` `repeat` `skip` `previous` `shuffle` `join` `leave`',inline=False)
        embed.add_field(name='Send Ảnh Động Vật',value='`catto` `doggo`',inline=False)
        embed.add_field(name='Send Ảnh Gái Alime',value='`neko` `kitsune`',inline=False)
        embed.add_field(name='Hololive Pic',value='`hololive` `sora` `miko` `Ĉ̷̹h̶͙̾r̶̒͜i̵͇̊ṡ̶͇` `aki` `suisei` `roboco` `fubuki` `matsuri` `aqua` `shion` `haachama` `ayame` `choco` `subaru` `AZKi` `mio` `okayu` `korone` `pekora` `rushia` `marine` `flare` `noel`  `coco`  `kanata`  `watame`  `towa`  `luna` `lamy`  `nene`  `botan`  `polka`  `aloe` ',inline=False)
        embed.add_field(name='Hololive ID',value='`risu` `moona` `iofi` `ollie` `anya` `reine`',inline=False)
        embed.add_field(name='Hololive EN',value='`mori` `kiara` `gura` `ina` `amelia` `irys` `sana` `fauna` `kronii` `mumei` `baelz`',inline=False)
        embed.add_field(name='Hololive CN',value='`yogiri` `civia` `echo` `doris` `rosalyn` `artia`',inline=False)
        embed.add_field(name='Other',value='`help` `ui` `wiki` `translate` `ping` `wink` `pat` `hug`',inline=False)
        embed.add_field(name='Bot Owner: Toji#9091',value='Please DMS Me if there are any errors (´ ∀ ` *)',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_8ball(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh 8ball*',
            description = 'Hỏi amelia',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài*',value='.8ball <câu hỏi>',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_meme(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh 8ball*',
            description = 'Gửi meme từ reddit',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.meme',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_play(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Play*',
            description = 'Phát Nhạc',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.play <tên bài hát/url>',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='Hãy Vô 1 Voice Channel Trước Khi xài',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_vanmau(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Văn Mẫu*',
            description = 'Send Văn',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.vanmau',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_stop(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Stop*',
            description = 'Dừng Nhạc',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.stop',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='Nó Sẽ Xóa Cả Queue Nên Hãy Xài .pause Nếu Muốn Dừng Nhạc Tạm Thời',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_queue(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Queue*',
            description = 'Queue Nhạc Của Bạn',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.queue',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_nowplaying(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Xem Bài Đang Phát*',
            description = 'Như Tên',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.nowplaying',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_repeat(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Repeat(loop)*',
            description = 'Phát Lại Cả Queue Hoặc 1 Bài',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.repeat <1/all>',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='1: Là repeat bài đang phát,all: Là cả Queue',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_skip(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Skip*',
            description = 'Skip tới bài tiếp theo',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.skip',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_previous(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Previous*',
            description = 'Phát Lại Bài Trước Đó',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.previous',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_shuffle(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Shuffle*',
            description = 'Trộn Nhạc',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.shuffle',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_join(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Join*',
            description = 'Join 1 Voice Channel',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.join',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='Nhớ vô voice channel trước nha cha',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_leave(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh leave*',
            description = 'Out Voice Channel',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.leave',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_neko(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Gửi Gái Tai Mèo*',
            description = 'nyan nyan nyan nyan',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.neko',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_help(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh help*',
            description = 'Bruh',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.help',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_kitsune(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Gửi Gái Tai Cáo*',
            description = 'kon kon kon',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.kitsune',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_ui(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Thông Tin Người Dùng*',
            description = 'Đẹp Trai/Gái Lắm UwU',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.ui',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_wiki(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Wiki*',
            description = 'Tra Wiki',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.wiki <thông tin cần tra>',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='Thằng Toji Code Lệnh Này Ngu Lắm Đừng Xài ~ Amelia',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_translate(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Dịch*',
            description = 'Dịch Từ Google Translate api Nên Dịch Ngu Đừng Hỏi',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.translate <mã ngôn ngữ> <câu cần dịch>',inline=False)
        embed.add_field(name='*Mã Ngôn Ngữ:*',value='Lấy 2 Chữ Cái Đầu Của Ngôn Ngữ Đó Bằng Tiếng Anh VD: vi(Vietnam)',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_ping(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Ping*',
            description = 'Pong !',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.ping',inline=False)
        embed.add_field(name='*Lưu Ý:*',value='Chỉ là tốc độ reply tin của bot thôi xd',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_catto(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Catto*',
            description = 'Gửi Mòe',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.catto',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_doggo(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Doggo*',
            description = 'Gửi Chóa',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.doggo',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_wink(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Wink*',
            description = 'wink wink wink',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.wink',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_pat(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Pat*',
            description = 'Pat Yah Head',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.pat',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_hug(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Hug*',
            description = 'ôm',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.hug',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command(invoke_without_commands=True)
    async def help_say(self,ctx,*,user: discord.Member = None):
        member = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed= discord.Embed(
            title = '*Lệnh Say*',
            description = 'Amelia Nói Địt Mẹ Mày',
            color = discord.Color.blurple())
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name='*Cách Xài:*',value='.say <câu j đó>',inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Yêu Cầu Bởi {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    


    
def setup(bot):
    bot.add_cog(helpCog(bot))
    
    


    
        