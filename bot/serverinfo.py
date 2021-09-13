import discord
from discord.ext import commands
from datetime import datetime
import locale
from utils import Config
from translates import Info, guild_not_found

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=['sinfo', 'sf'])
    async def serverinfo(self, ctx, guild: int=None):
        language = Config(ctx.guild).language
        messages = Info(language=language)
        guild =  self.client.get_guild(guild) if guild else ctx.guild
        if not guild:
            return await ctx.message.reply(guild_not_found(language=language))
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        boost = self.client.get_emoji(841285825282048011)
        embed=discord.Embed(title=f"**{guild.name}**", color=0x2f3136)
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name=messages.owner, value=f"`{guild.owner}`", inline=True)
        embed.add_field(name=messages.region, value=f"{guild.region}", inline=True)
        embed.add_field(name=messages.creation_date, value=f"{guild.created_at.strftime('%d de %B de %Y')}", inline=True)
        embed.add_field(name=messages.members, value=f"`{guild.member_count}`", inline=True)
        if ctx.author in guild.members:
            embed.add_field(name=messages.join_date, value=f"{guild.get_member(ctx.author.id).joined_at.strftime('%d de %B de %Y')}", inline=True)
        embed.add_field(name=f"{boost}  Boost level:", value=f"Level {guild.premium_tier}", inline=True)
        if guild.banner_url:
            embed.set_image(url=ctx.guild.banner_url)
        embed.timestamp = datetime.utcnow()
        message = await ctx.message.reply(embed=embed)
        await message.add_reaction("❌")
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        reaction, _ = await self.client.wait_for('reaction_add', check=check, timeout=60.)
        if reaction.emoji == '❌':
            try:
                await ctx.message.delete()
            except:
                pass
            await message.delete()


def setup(client):
    client.add_cog(ServerInfo(client))