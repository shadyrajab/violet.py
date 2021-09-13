import discord
from discord.ext import commands
import typing
from utils import Config
from translates import user_not_found

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['icon'])
    async def avatar(self, ctx, member: typing.Union[discord.User, int, str]=None):
        member = ctx.author if not member else member
        member = await self.client.fetch_user(member) if isinstance(member, int) else member
        if isinstance(member, str):
            return await ctx.message.reply(user_not_found(language=Config(ctx.guild).language))
        embed = discord.Embed(title=member.name, color=0x2f3136)
        embed.set_image(url=member.avatar_url)
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
    client.add_cog(Avatar(client))