import discord
from discord.ext import commands
from datetime import datetime
import locale
from utils import Config
from translates import Info

class UserInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['uinfo', 'uf'])
    @commands.guild_only()
    async def userinfo(self, ctx, user: discord.Member=None):
        language = Config(ctx.guild).language
        messages = Info(language=language)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        member = user if user else ctx.author
        owner = '👑' if member == ctx.guild.owner else ''
        bug_hunter = self.client.get_emoji(841285825743552512)\
            if member.public_flags.bug_hunter or member.public_flags.bug_hunter_level_2 else ''
        partner = self.client.get_emoji(841285825664122910)\
            if member.public_flags.partner else ''
        verified_bot_developer = self.client.get_emoji(841285825370259518)\
            if member.public_flags.verified_bot_developer or member.public_flags.early_verified_bot_developer else ''
        hypesquad_house = self.client.get_emoji(841285825391624203)\
            if member.public_flags.hypesquad_brilliance else ''
        hypesquad_house = self.client.get_emoji(841285825513390110)\
            if member.public_flags.hypesquad_bravery else hypesquad_house
        hypesquad_house = self.client.get_emoji(841285825525973062)\
            if member.public_flags.hypesquad_balance else hypesquad_house
        roles = []
        for role in member.roles:
            if role.name == '@everyone' or role == member.top_role:
                continue
            roles.append(role.mention)
        roles.reverse()
        embed=discord.Embed(title=f"{owner}{verified_bot_developer}{bug_hunter}{partner}{hypesquad_house} **{member.name}**", color=0x2f3136)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_author(name=f"", icon_url=f"{member.avatar_url}")
        embed.add_field(name="🧾 Tag:", value=f"`{member}`", inline=True)
        embed.add_field(name='📎 ID:', value=f'`{member.id}`')
        embed.add_field(name=messages.creation_date, value=f"{member.created_at.strftime('%d de %B de %Y')}", inline=True)
        embed.add_field(name=messages.join_date, value=f"{member.joined_at.strftime('%d de %B de %Y')}", inline=True)
        if member.top_role.name != '@everyone':
            embed.add_field(name=messages.main_role, value=f"{member.top_role.mention}", inline=True)
        if member.premium_since:
            boost = self.client.get_emoji(841285825282048011)
            embed.add_field(name=boost + messages.booster_since, value=f"{member.premium_since.strftime('%d de %B de %Y')}", inline = True)
        if len(roles) != 0:
            embed.add_field(name=messages.secondary_roles, value=", ".join(roles), inline=False)
        embed.timestamp = datetime.now()
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
    client.add_cog(UserInfo(client))