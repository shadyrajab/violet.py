from discord.ext import commands
import discord
from datetime import datetime
from utils import Config
from translates import HelpMessages

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ajuda', 'ayuda', 'commands', 'comandos', 'comando', 'command'])
    async def help(self, ctx, category=None):
        bot = await self.client.fetch_user(705474553983533178)
        prefix = Config(ctx.guild).prefix if isinstance(ctx.message.channel, discord.TextChannel) else ''
        messages = HelpMessages(language=Config(ctx.guild).language, prefix=prefix)
        if not category or category.lower() == 'help' or category.lower() in self.client.get_command('help').aliases:
            embed = discord.Embed(description=messages.get_command, color=0x2f3136)
            embed.add_field(name=messages.temporary_rooms, value='``trsetup``, ``trdisable``, ``trename``, ``trlock``, ``trunlock``, ``tradd``, ``tremove``, ``tresetadmin``, ``tremoveadmin``, ``trblock``, ``trunblock``, ``trhide``, ``trunhide``, `trsetowner`, `presets`', inline=False)
            embed.add_field(name=messages.moderation, value='``ban``, ``kick``, ``mute``, ``lock``, ``clear``', inline=False)
            embed.add_field(name=messages.utility, value='``userinfo``, ``serverinfo``, ``avatar``, ``remindme``', inline=False)
            embed.add_field(name=messages.games, value='``namemc``')
            embed.add_field(name=messages.configuration, value='``changeprefix``, ``language``', inline=False)
            embed.add_field(name=f'ㅤ', value=messages.invite, inline=False)
            embed.set_author(name='Help', icon_url=f'{bot.avatar_url}', url='https://discord.com/api/oauth2/authorize?client_id=862740130385494027&permissions=286616662&scope=bot')
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='Violet')
            return await ctx.message.reply(embed=embed)
        description, examples = None, None
        if category.lower() == 'ban' or category.lower() in self.client.get_command('ban').aliases:
            description = messages.ban
            use = f'''``{prefix}ban <@member> [reason]``
            ``{prefix}ban <member_id> [reason]``'''
            examples = messages.ban_examples
            permissions = messages.ban_permission
            parents = True
        if category.lower() == 'mute' or category.lower() == 'unmute' or category.lower() in self.client.get_command('mute').aliases or category.lower() in self.client.get_command('unmute').aliases:
            description = messages.mute
            use = f'``{prefix}mute <@member> [reason]``'
            examples = messages.mute_examples
            permissions = messages.kick_permission
            parents = True
        if category.lower() == 'kick' or category.lower() in self.client.get_command('kick').aliases:
            description = messages.kick
            use = f'''``{prefix}kick <@member> [motivo]``
            ``{prefix}kick <member_id> [motivo]``'''
            examples = messages.kick_examples
            permissions = messages.kick_permission
            parents = True
        if category.lower() == 'clear' or category.lower() in self.client.get_command('clear').aliases:
            description = messages.clear
            use = f'``{prefix}clear <messages>``'
            permissions = messages.manage_messages_permission
            parents = True
        if category.lower() == 'lock' or category.lower() == 'unlock' or category.lower() in self.client.get_command('lock').aliases or category.lower() in self.client.get_command('unlock').aliases:
            description = messages.lock
            use = f'``{prefix}lock [channel]``'
            examples = messages.lock_examples
            permissions = messages.manage_channel_permission
            parents = True
        if category.lower() == 'avatar' or category.lower() in self.client.get_command('avatar').aliases:
            description = messages.avatar
            use = f'``{prefix}avatar [user]``'
            examples = messages.avatar_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'namemc' or category.lower() in self.client.get_command('namemc').aliases:
            description = messages.namemc
            use = f'``{prefix}namemc <nick>``'
            examples = messages.namemc_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'remindme' or category.lower() in self.client.get_command('remindme').aliases:
            description = messages.remindme
            use = f'``{prefix}remindme <remind>``'
            examples = messages.remindme_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'servericon' or category.lower() in self.client.get_command('servericon').aliases:
            description = messages.servericon
            use = f'''``{prefix}servericon [server_id]``'''
            examples = messages.remindme_examples 
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'serverinfo' or category.lower() in self.client.get_command('serverinfo').aliases:
            description = messages.serverinfo
            use = f'``{prefix}serverinfo [server]``'
            examples = messages.userinfo_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'userinfo' or category.lower() in self.client.get_command('userinfo').aliases:
            description = messages.userinfo
            use = f'``{prefix}userinfo [member]``'
            examples = messages.userinfo_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'presets' or category.lower() in self.client.get_command('presets').aliases:
            description = messages.presets
            use = f'``{prefix}presets [server]``'
            examples = messages.presets_examples
            permissions = messages.without_permissions
            parents = True
        if category.lower() == 'trsetup' or category.lower() == 'trdisable' or category.lower() in self.client.get_command('trsetup').aliases or category.lower() in self.client.get_command('trdisable').aliases:
            description = messages.trsetup
            use = f'``{prefix}trsetup``'
            permissions = messages.setup_permission
            parents = False
        if category.lower() == 'trename' or category.lower() in self.client.get_command('trename').aliases:
            description = messages.trename
            use = f'``{prefix}trename <name>``'
            permissions = messages.channel_admin_permission
            parents = True
        if category.lower() == 'trlock' or category.lower() == 'trunlock' or category.lower() in self.client.get_command('trlock').aliases or category.lower() in self.client.get_command('trunlock').aliases:
            description = messages.trlock
            use = f'``{prefix}trlock``'
            permissions = messages.channel_admin_permission
            parents = False
        if category.lower() == 'tradd' or category.lower() == 'tremove' or category.lower() in self.client.get_command('tradd').aliases or category.lower() in self.client.get_command('tremove').aliases:
            description = messages.tradd
            use = f'``{prefix}tradd <member>``'
            examples = messages.tradd_examples
            permissions = messages.channel_admin_permission
            parents = True 
        if category.lower() == 'trhide' or category.lower() == 'trunhide' or category.lower() in self.client.get_command('trhide').aliases or category.lower() in self.client.get_command('trunhide').aliases:
            description = messages.trhide
            use = f'``{prefix}trhide``'
            permissions = messages.channel_admin_permission
            parents = False
        if category.lower() == 'trblock' or category.lower() == 'trunblock' or category.lower() in self.client.get_command('trblock').aliases or category.lower() in self.client.get_command('trunblock').aliases:
            description = messages.trblock
            use = f'``{prefix}trblock <member>``'
            examples = messages.trblock_examples
            permissions = messages.channel_admin_permission
            parents = True
        if category.lower() == 'trsetadmin' or category.lower() == 'tremoveadmin' or category.lower() in self.client.get_command('trsetadmin').aliases or category.lower() in self.client.get_command('tremoveadmin').aliases:
            description = messages.trsetadmin
            use = f'``{prefix}trsetadmin <member>``'
            examples = messages.trsetadmin_examples
            permissions = messages.channel_owner_permission
            parents = True
        if category.lower() == 'trsetowner' or category.lower() in self.client.get_command('trsetowner').aliases:
            description = messages.trsetowner
            use = f'``{prefix}trsetowner <member>``'
            examples = messages.trsetowner_examples
            permissions = messages.channel_owner_permission
            parents = True
        if not description:
            return await ctx.message.reply(messages.command_not_found)
        embed = discord.Embed(description=description, color=0x2f3136)
        embed.set_author(name=f'{prefix}{category}', icon_url=bot.avatar_url)
        embed.add_field(name=messages.use, value=use, inline=False)
        if examples:
            embed.add_field(name=messages.examples, value=examples, inline=False)
        embed.add_field(name=messages.permissions, value=permissions, inline=False)
        if self.client.get_command(category.lower()).aliases:
            alias = f', '.join(f'``{prefix}{alias}``' for alias in self.client.get_command(category).aliases)
            embed.add_field(name=messages.alias, value=f'{alias}', inline=False)
        if parents:
            embed.add_field(name='ㅤ', value=messages.arguments, inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='Violet')
        await ctx.message.reply(embed=embed)
        

def setup(client):
    client.add_cog(Help(client))