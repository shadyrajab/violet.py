import json
import discord
from discord.ext import commands
import utils
import typing
from utils import Config
import functools
import asyncio
from datetime import datetime
from .presets import Presets
import requests
from translates import TemporaryRoomsMessages, user_or_role_not_found

class Room():
    def __init__(self, ctx, channel):
        self.channel = channel
        self.ctx = ctx if isinstance(ctx, discord.Member) else ctx.author
        with open('bot/temporaryrooms/rooms.json', 'r') as f:
            self.rooms = json.load(f)
        try:
            self.room = self.rooms[str(self.channel.id)]
        except KeyError:
            self.rooms[str(channel.id)] = {
                "owner": self.ctx.id,
                "admins": []
            }
            with open('bot/temporaryrooms/rooms.json', 'w') as f:
                json.dump(self.rooms, f, indent=4)
            
            self.room = self.rooms[str(self.channel.id)]

    def delete(self):
        self.rooms.pop(str(self.channel.id))
        with open('bot/temporaryrooms/rooms.json', 'w') as f:
            json.dump(self.rooms, f, indent=4)

    def set_owner(self, owner):
        self.room["owner"] = owner
        with open('bot/temporaryrooms/rooms.json', 'w') as f:
            json.dump(self.rooms, f, indent=4)

    def add_admin(self, admin):
        self.room["admins"].append(admin)
        with open('bot/temporaryrooms/rooms.json', 'w') as f:
            json.dump(self.rooms, f, indent=4)
    
    def remove_admin(self, admin):
        self.rooms["admins"].remove(admin)
        with open('bot/temporaryrooms/rooms.json', 'w') as f:
            json.dump(self.rooms, f, indent=4)

    @staticmethod
    def is_troom(func):
        @functools.wraps(func)
        async def check(*args):
            with open('bot/temporaryrooms/rooms.json', 'r') as f:
                rooms = json.load(f)

            ctx = args[1]
            if ctx.author.voice and str(ctx.author.voice.channel.id) in rooms:
                await func(*args)
            else:
                messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
                embed=discord.Embed(color=0x2f3136)
                embed.set_author(name=ctx.author.voice.channel.name if ctx.author.voice else 'ㅤ', icon_url=ctx.author.avatar_url)
                embed.add_field(name='ㅤ', value=messages.not_connected)
                embed.timestamp = datetime.utcnow()
                await ctx.message.reply(embed=embed)

        return check

    @staticmethod
    def is_owner(func):
        @functools.wraps(func)
        async def check(*args):
            with open('bot/temporaryrooms/rooms.json', 'r') as f:
                rooms = json.load(f)

            ctx = args[1]
            if ctx.author.id == rooms[str(ctx.author.voice.channel.id)]["owner"]:
                await func(*args)
            else:
                messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
                embed=discord.Embed(color=0x2f3136)
                embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name='ㅤ', value=messages.not_owner)
                embed.timestamp = datetime.utcnow()
                await ctx.message.reply(embed=embed)
                
        return check

    @staticmethod
    def is_admin(func):
        @functools.wraps(func)
        async def check(*args):
            with open('bot/temporaryrooms/rooms.json', 'r') as f:
                rooms = json.load(f)

            ctx = args[1]
            if ctx.author.id in rooms[str(ctx.author.voice.channel.id)]["admins"] or \
                ctx.author.id == rooms[str(ctx.author.voice.channel.id)]["owner"]:
                await func(*args)
            else:
                messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
                embed=discord.Embed(color=0x2f3136)
                embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name='ㅤ', value=messages.not_admin)
                embed.timestamp = datetime.utcnow()
                await ctx.message.reply(embed=embed)
        
        return check
        
    @staticmethod
    def check_rooms(func):
        @functools.wraps(func)
        async def check(*args):
            with open('bot/temporaryrooms/rooms.json', 'r') as f:
                rooms = json.load(f)

            member = args[1]
            config = Config(member.guild)
            len_rooms = 1
            if member.voice and member.voice.channel.id == config.channel_id:
                for room in rooms:
                    owner = rooms[room]["owner"]
                    if owner == member.id:
                        len_rooms += 1

            if len_rooms <= 3:
                await func(*args)
            else:
                await member.move_to(channel=None)
                try:
                    messages = TemporaryRoomsMessages(language=Config(member.guild).language, member=member)
                    await member.send(messages.channel_limit)
                except discord.Forbidden:
                    pass
        
        return check


class TemporaryChannels(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def trsetup(self, ctx):
        url = 'https://jsonstorage.net/api/items/b1548f01-fd49-484b-be8c-3e2815520b15'
        config = requests.get(url).json()
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not config[str(ctx.guild.id)]["category_id"]:
            category = await ctx.guild.create_category("Salas temporárias")
            channel = await category.create_voice_channel("Entre aqui")
            config[str(ctx.guild.id)]["category_id"] = category.id
            config[str(ctx.guild.id)]["channel_id"] = channel.id

            headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
            new_data = json.dumps(config)
            requests.put(url, headers=headers, data=new_data)
            await ctx.message.reply(messages.setup)
            await utils.send_configs(self.client)
        else:
            await ctx.message.reply(messages.already_activated)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def trdisable(self, ctx):
        url = 'https://jsonstorage.net/api/items/b1548f01-fd49-484b-be8c-3e2815520b15'
        config = requests.get(url).json()
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if config[str(ctx.guild.id)]["category_id"]:
            try:
                await ctx.guild.get_channel(config[str(ctx.guild.id)]["category_id"]).delete()
                await ctx.guild.get_channel(config[str(ctx.guild.id)]["channel_id"]).delete()
            except:
                pass
            config[str(ctx.guild.id)]["category_id"] = None
            config[str(ctx.guild.id)]["channel_id"] = None

            headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
            new_data = json.dumps(config)
            requests.put(url, headers=headers, data=new_data)
            await utils.send_configs(self.client)
            await ctx.message.reply(messages.disable)
        else:
            await ctx.message.reply(messages.not_activated)

    @commands.Cog.listener()
    @Room.check_rooms
    async def on_voice_state_update(self, member: discord.Member, after: discord.VoiceState, before: discord.VoiceState):
        config = Config(member.guild)
        messages = TemporaryRoomsMessages(language=Config(member.guild).language, member=member)
        trchannel = member.guild.get_channel(config.channel_id)
        trcategory = member.guild.get_channel(config.category_id)
        if trchannel and trcategory:
            if member.voice and member.voice.channel.id == trchannel.id:
                try:
                    presets = Presets(ctx=member, guild=member.guild, client=self.client)
                except KeyError:
                    presets = None
                everyone = discord.utils.get(member.guild.roles, name='@everyone')
                channel = await trcategory.create_voice_channel(name=messages.room_name if not presets or \
                    presets.name == "default" else presets.name)
                await channel.set_permissions(target=member, connect=True, view_channel=True, manage_permissions=True, manage_channels=True)
                await member.move_to(channel=channel)
                room = Room(ctx=member, channel=channel)
                if presets and presets.hide or presets and presets.lock:
                    overwrites = channel.overwrites_for(everyone)
                    overwrites.connect = None if not presets or not presets.lock else False
                    overwrites.view_channel = None if not presets or not presets.hide else False
                    await channel.set_permissions(target=everyone, overwrite=overwrites)
                if presets and presets.members[0]:
                    for member_ in presets.members[0]:
                        await channel.set_permissions(target=member_, connect=True, view_channel=True)
                if presets and presets.admins[0]:
                    for admin in presets.admins[0]:
                        room.add_admin(admin.id)
                        await channel.set_permissions(target=admin, connect=True, view_channel=True, manage_channels=True, manage_permissions=True)
                if presets and presets.blocks[0]:
                    for block in presets.blocks[0]:
                        await channel.set_permissions(target=block, connect=False, view_channel=False)
        
            for channel in trcategory.voice_channels:
                if channel.id == trchannel.id or len(channel.members) != 0:
                    continue
                await asyncio.sleep(20)
                if len(channel.members) == 0:   
                    room = Room(ctx=member, channel=channel)
                    room.delete()
                    try:
                        await channel.delete()
                    except discord.NotFound:
                        pass

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trename(self, ctx, *name):
        if not name:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        name = ' '.join(name)
        embed = discord.Embed(color=0x2f3136)
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.rename + f' `{name}`')
        embed.timestamp = datetime.utcnow()
        await ctx.author.voice.channel.edit(name=name)
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trlock(self, ctx):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        everyone = discord.utils.get(ctx.guild.roles, name="@everyone")
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.lock)
        embed.timestamp = datetime.utcnow()
        overwrites = ctx.author.voice.channel.overwrites_for(everyone)
        overwrites.connect = False
        await ctx.author.voice.channel.set_permissions(target=everyone, overwrite=overwrites)
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trunlock(self, ctx):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        everyone = discord.utils.get(ctx.guild.roles, name="@everyone")
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.unlock)
        embed.timestamp = datetime.utcnow()
        overwrites = ctx.author.voice.channel.overwrites_for(everyone)
        overwrites.connect = None
        await ctx.author.voice.channel.set_permissions(target=everyone, overwrite=overwrites)
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trhide(self, ctx):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        everyone = discord.utils.get(ctx.guild.roles, name="@everyone")
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.hide)
        embed.timestamp = datetime.utcnow()
        overwrites = ctx.author.voice.channel.overwrites_for(everyone)
        overwrites.view_channel = False
        await ctx.author.voice.channel.set_permissions(target=everyone, overwrite=overwrites)
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trunhide(self, ctx):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        everyone = discord.utils.get(ctx.guild.roles, name="@everyone")
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.unhide)
        embed.timestamp = datetime.utcnow()
        overwrites = ctx.author.voice.channel.overwrites_for(everyone)
        overwrites.view_channel = None
        await ctx.author.voice.channel.set_permissions(target=everyone, overwrite=overwrites)
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trblock(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        bot = await self.client.fetch_user(705474553983533178)
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        blocks = []
        mentions = []
        notfound = []
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    if member == ctx.author:
                        await ctx.message.reply(messages.block_herself)
                        continue
                    if member == bot:
                        await ctx.message.reply(messages.block_bot)
                        channel = ctx.author.voice.channel
                        await channel.connect()
                    blocks.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                blocks.append(member_)
        if notfound:
            a = " , ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if blocks:
            for member in blocks:
                mentions.append(member.mention)
                overwrites = ctx.author.voice.channel.overwrites_for(member)
                overwrites.connect = False
                await ctx.author.voice.channel.set_permissions(target=member, overwrite=overwrites)
                if isinstance(member, discord.Member) and member.voice:
                    await member.move_to(channel=None)
                if isinstance(member, discord.Role):
                    for member_ in member.members:
                        if member_.voice and member_.voice.channel == ctx.author.voice.channel:
                            if member_ == ctx.author:
                                continue
                            await member_.move_to(channel=None)
            embed.add_field(name='ㅤ', value=messages.block(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def trunblock(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        unblocks = []
        mentions = []
        notfound = []
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    unblocks.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                unblocks.append(member_)
        if notfound:
            a = ", ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if unblocks:
            for member in unblocks:
                if member in ctx.author.roles or ctx.author == member:
                    continue
                mentions.append(member.mention)
                overwrites = ctx.author.voice.channel.overwrites_for(member)
                overwrites.connect = None
                await ctx.author.voice.channel.set_permissions(target=member, overwrite=overwrites)
            embed=discord.Embed(color=0x2f3136)
            embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='ㅤ', value=messages.unblock(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def tradd(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        adds = []
        mentions = []
        notfound = []
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    adds.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                adds.append(member_)
        if notfound:
            a = ", ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if adds:
            for member in adds:
                mentions.append(member.mention)
                overwrites = ctx.author.voice.channel.overwrites_for(member)
                overwrites.connect = True
                overwrites.view_channel = True
                await ctx.author.voice.channel.set_permissions(target=member, overwrite=overwrites)
            embed=discord.Embed(color=0x2f3136)
            embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='ㅤ', value=messages.add(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_admin
    async def tremove(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        removes = []
        mentions = []
        notfound = []
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    removes.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                removes.append(member_)
        if notfound:
            a = ", ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if removes:
            for member in removes:
                mentions.append(member.mention)
                await ctx.author.voice.channel.set_permissions(target=member, overwrite=None)
            embed=discord.Embed(color=0x2f3136)
            embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='ㅤ', value=messages.remove(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_owner
    async def trsetadmin(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        admins = []
        mentions = []
        notfound = []
        room = Room(ctx=ctx, channel=ctx.author.voice.channel)
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    admins.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                admins.append(member_)
        if notfound:
            a = ", ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if admins:
            for member in admins:
                mentions.append(member.mention)
                room.add_admin(member.id)
                await ctx.author.voice.channel.set_permissions(target=member, connect=True, view_channel=True, manage_permissions=True, manage_channels=True)
            embed=discord.Embed(color=0x2f3136)
            embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='ㅤ', value=messages.set_admin(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_owner
    async def tremoveadmin(self, ctx, *args: typing.Union[discord.Member, discord.Role, str]):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language)
        if not args:
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        admins = []
        mentions = []
        notfound = []
        room = Room(ctx=ctx, channel=ctx.author.voice.channel)
        for member_ in args:
            if isinstance(member_, str):
                member = ctx.guild.get_member_named(member_)
                member = ctx.guild.get_role(member_) if not member else member
                if member:
                    admins.append(member)  
                    mentions.append(member.mention) 
                else:
                    notfound.append(member_)
            else:
                admins.append(member_)
        if notfound:
            a = ", ".join(notfound)
            await ctx.message.reply(user_or_role_not_found + f'`{a}`')
            if len(args) == 1:
                return
        if admins:
            for member in admins:
                mentions.append(member.mention)
                room.remove_admin(member.id)
                await ctx.author.voice.channel.set_permissions(target=member, overwrite=None)
            embed=discord.Embed(color=0x2f3136)
            embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='ㅤ', value=messages.remove_admin(mentions))
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

    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @Room.is_troom
    @Room.is_owner
    async def trsetowner(self, ctx, owner: discord.Member):
        messages = TemporaryRoomsMessages(language=Config(ctx.guild).language, member=owner)
        room = Room(ctx=ctx, channel=ctx.author.voice.channel)
        room.set_owner(owner.id)
        embed=discord.Embed(color=0x2f3136)
        embed.set_author(name=ctx.author.voice.channel.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='ㅤ', value=messages.set_owner)
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

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        with open('bot/temporaryrooms/rooms.json', 'r') as f:
            rooms = json.load(f)

        if str(channel.id) in rooms:
            rooms.pop(str(channel.id))
        
        with open('bot/temporaryrooms/rooms.json', 'w') as f:
            json.dump(rooms, f, indent=4)


def setup(client):
    client.add_cog(TemporaryChannels(client))