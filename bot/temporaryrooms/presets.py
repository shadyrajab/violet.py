import json
import discord
from discord.ext import commands
import utils
import requests
from translates import PresetsMessages, user_or_role_not_found
import dotenv
from os import getenv

class Presets():
    def __init__(self, ctx, guild, client=None):
        self.ctx = ctx if isinstance(ctx, discord.Member) else ctx.author
        self.client = client
        self.guild = guild
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.url = f'https://jsonstorage.net/api/items/{getenv("Presets")}'
        self.presets = requests.get(self.url).json()
        
        if guild:
            self.presets_ = self.presets[str(self.ctx.id)][str(self.guild.id)]

    async def set_name(self, name):
        self.presets_["name"] = name
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)
        await utils.send_presets(self.client)
         
    async def set_lock(self, value):
        self.presets_["lock"] = value
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)
        await utils.send_presets(self.client)

    async def set_hide(self, value):
        self.presets_["hide"] = value
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)     
        await utils.send_presets(self.client)   

    async def add_member(self, member):
        self.presets_["members"].append(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data) 
        await utils.send_presets(self.client)        

    async def add_admin(self, member):
        self.presets_["admins"].append(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data) 
        await utils.send_presets(self.client)       
    
    async def remove_member(self, member):
        self.presets_["members"].remove(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data) 
        await utils.send_presets(self.client)    
    
    async def remove_admin(self, member):
        self.presets_["admins"].remove(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)   
        await utils.send_presets(self.client)  

    async def block_member(self, member):
        self.presets_["blocks"].append(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)
        await utils.send_presets(self.client)
    
    async def unblock_member(self, member):
        self.presets_["blocks"].remove(str(member))
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        new_data = json.dumps(self.presets)
        requests.put(self.url, headers=headers, data=new_data)
        await utils.send_presets(self.client)
        
    @property
    def name(self):
        name = self.presets_["name"]
        return f"Sala de {self.ctx.name}" if name == "default" else name
    
    @property
    def hide(self):
        hide = self.presets_["hide"]
        return hide

    @property
    def lock(self):
        lock = self.presets_["lock"]
        return lock

    @property
    def members(self):
        members_ = []
        mentions = []
        members = self.presets_["members"]
        for member in members:
            user = self.client.get_user(int(member))
            user = self.ctx.guild.get_role(int(member)) if not user else user
            if isinstance(user, type(None)):
                members.remove(member)
                headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
                new_data = json.dumps(self.presets)
                requests.put(self.url, headers=headers, data=new_data)
                continue
            members_.append(user)
            mentions.append(user.mention)
        members_, mentions = None if len(members_) == 0 else members_, mentions
        return members_, mentions

    @property
    def admins(self):
        admins_ = []
        mentions = []
        admins = self.presets_["admins"]
        for member in admins:
            user = self.client.get_user(int(member))
            user = self.ctx.guild.get_role(int(member)) if not user else user
            if isinstance(user, type(None)):
                admins.remove(member)
                headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
                new_data = json.dumps(self.presets)
                requests.put(self.url, headers=headers, data=new_data)
                continue
            admins_.append(user)
            mentions.append(user.mention)
        admins_, mentions = None if len(admins_) == 0 else admins_, mentions
        return admins_, mentions
    
    @property
    def blocks(self):
        blocks_ = []
        mentions = []
        blocks = self.presets_["blocks"]
        for member in blocks:
            user = self.client.get_user(int(member))
            user = self.ctx.guild.get_role(int(member)) if not user else user
            if isinstance(user, type(None)):
                blocks.remove(member)
                headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
                new_data = json.dumps(self.presets)
                requests.put(self.url, headers=headers, data=new_data)
                continue
            blocks_.append(user)
            mentions.append(user.mention)
        blocks_, mentions = None if len(blocks_) == 0 else blocks_, mentions
        return blocks_, mentions


class TRConfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def presets(self, ctx, guild=None):
        bot = await self.client.fetch_user(705474553983533178)
        guild =  await self.client.fetch_guild(guild) if guild else ctx.guild
        messages = PresetsMessages(language=utils.Config(ctx.guild).language, ctx=ctx)
        async def send_configs():
            def check(reaction, user):
                return user == ctx.author and reaction.emoji and reaction.message.id == message.id

            def check_(message):
                return message.author == ctx.author and message.channel == ctx.channel  
            presets = Presets(ctx, guild, self.client)
            embed = discord.Embed(title='', color=0x2f3136)
            embed.set_author(name=messages.default, icon_url=ctx.author.avatar_url)
            embed.add_field(name=messages.room_name, value=f"[{presets.name}](https://discord.com/api/oauth2/authorize?client_id=705474553983533178&permissions=8&scope=bot)", inline=True)
            embed.add_field(name=messages.locked, value=f"[{presets.lock}](https://discord.com/api/oauth2/authorize?client_id=705474553983533178&permissions=8&scope=bot)", inline=True)
            embed.add_field(name=messages.invisible, value=f"[{presets.hide}](https://discord.com/api/oauth2/authorize?client_id=705474553983533178&permissions=8&scope=bot)", inline=False)
            embed.add_field(name=messages.members, value="\n".join(presets.members[1]) if presets.members[1] else 'ㅤ', inline=True)
            embed.add_field(name=messages.admins, value="\n".join(presets.admins[1]) if presets.admins[1] else 'ㅤ', inline=True)
            embed.add_field(name=messages.blockeds, value="\n".join(presets.blocks[1]) if presets.blocks[1] else 'ㅤ', inline=False)
            embed.add_field(name='ㅤ', value=messages.category)
            embed.set_footer(text=messages.obs, icon_url=bot.avatar_url)
            message = await ctx.message.reply(embed=embed)
            await message.add_reaction("📄")
            await message.add_reaction("🔒") if not presets.lock else await message.add_reaction("🔓")
            await message.add_reaction("🔗") if not presets.hide else await message.add_reaction("🧷")
            await message.add_reaction("👥")
            await message.add_reaction("👑")
            await message.add_reaction("❌")
            await message.add_reaction("🚫")

            while True:
                reaction, _user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
                if reaction.emoji == "📄":
                    await ctx.send(messages.what_name)
                    name = await self.client.wait_for("message", check=check_, timeout=60.0)
                    if len(name.system_content) < 25:
                        await presets.set_name(name.system_content)
                        await name.reply(messages.name_changed + f' `{name.system_content}`')
                    else:
                        await name.reply(messages.exceed)
                if reaction.emoji == "🔒" or reaction.emoji == "🔓":
                    await presets.set_lock(False) if presets.lock else await presets.set_lock(True)
                    await ctx.message.reply(messages.set_lock + f' `{presets.lock}`')
                if reaction.emoji == "🔗" or reaction.emoji == "🧷":
                    await presets.set_hide(False) if presets.hide else await presets.set_hide(True)
                    await ctx.message.reply(messages.set_hide + f' `{presets.hide}`')
                if reaction.emoji == "👥":
                    message = await ctx.send(messages.add_members)
                    await message.add_reaction("🟢")
                    await message.add_reaction("🔴")
                    reaction, _user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
                    if reaction.emoji == "🟢":
                        await ctx.send(messages.add_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.add_member(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))    
                                await presets.add_member(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.add_member(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member)
                                    else:
                                        await presets.add_member(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(", ".join(resp) + messages.members_added)
                    
                    if reaction.emoji == "🔴":
                        await ctx.send(messages.remove_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.remove_member(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))    
                                await presets.remove_member(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.remove_member(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member_)
                                    else:
                                        await presets.remove_member(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(", ".join(resp) + messages.members_removed) 
                
                if reaction.emoji == "👑":
                    message = await ctx.send(messages.add_admins)
                    await message.add_reaction("🟢")
                    await message.add_reaction("🔴")
                    reaction, _user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
                    if reaction.emoji == "🟢":
                        await ctx.send(messages.add_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.add_admin(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))    
                                await presets.add_admin(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.add_admin(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member)
                                    else:
                                        await presets.add_admin(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(", ".join(resp) + messages.admins_added)
                    
                    if reaction.emoji == "🔴":
                        await ctx.send(messages.remove_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.remove_admin(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))    
                                await presets.remove_admin(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.remove_admin(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member)
                                    else:
                                        await presets.remove_admin(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(" , ".join(resp) + messages.admins_removed)
                if reaction.emoji == "❌":
                    message = await ctx.send(messages.block_members)
                    await message.add_reaction("🔴")
                    await message.add_reaction("🟢")
                    reaction, _user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
                    if reaction.emoji == "🔴":
                        await ctx.send(messages.block_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.block_member(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))    
                                await presets.block_member(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.block_member(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member)
                                    else:
                                        await presets.block_member(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(", ".join(resp) + messages.blocked)
                    
                    if reaction.emoji == "🟢":
                        await ctx.send(messages.unblock_who)
                        members_ = await self.client.wait_for("message", check=check_, timeout=60.0)
                        members = members_.system_content.split()
                        resp = []
                        notfound = []
                        for member in members:
                            if member.startswith("<@&"):
                                id = member.replace("<@&", "").replace(">", "")
                                role = guild.get_role(int(id))
                                await presets.unblock_member(str(role.id))
                                resp.append(str(f"`{role.name}`"))
                            elif member.startswith("<@!"):
                                id = member.replace("<@!", "").replace(">", "")  
                                member = guild.get_member(int(id))
                                await presets.unblock_member(str(member.id))     
                                resp.append(str(f"`{member}`"))
                            else:
                                try:
                                    member = guild.get_member(int(member)) if guild.get_member(int(member)) else member
                                    member = guild.get_role(int(member)) if not isinstance(member, discord.Member) else member
                                    await presets.unblock_member(str(member.id))  
                                    resp.append(str(f"`{member}`"))
                                except ValueError:
                                    member_ = guild.get_member_named(member)
                                    member_ = discord.utils.get(guild.roles, name=member) if not member_ else member_
                                    if not member_:
                                        notfound.append(member)
                                    else:
                                        await presets.unblock_member(str(member_.id))
                                        resp.append(str(f"`{member}`"))
                        if notfound:
                            a = " , ".join(notfound)
                            await members_.reply(user_or_role_not_found + a)
                        if resp:
                            await members_.reply(" , ".join(resp) + messages.unblocked)
                if reaction.emoji == "🚫":
                    message = await ctx.message.reply(messages.delete)
                    await message.add_reaction("✅")
                    reaction, _user = await self.client.wait_for("reaction_add", check=check)
                    if reaction.emoji == "✅":
                        url = f'https://jsonstorage.net/api/items/{getenv("Presets")}'
                        presets = requests.get(url).json()
                        presets.pop(str(ctx.author.id)) if len(presets[str(ctx.author.id)]) == 1 else presets[str(ctx.author.id)].pop(str(guild.id))
                        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
                        new_data = json.dumps(presets)
                        requests.put(url, headers=headers, data=new_data)
                        await ctx.message.reply(messages.deleted)
                        await utils.send_presets(self.client)
                         
        if not guild:
            return await ctx.message.reply(messages.inform)
        try:
            await send_configs()

        except KeyError:
            def check(reaction, user):
                return user == ctx.author and reaction.emoji and reaction.message.id == message.id
            message = await ctx.message.reply(messages.not_presets)
            await message.add_reaction("✔️")

            reaction, _user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
            if reaction.emoji == "✔️":
                url = f'https://jsonstorage.net/api/items/{getenv("Presets")}'
                presets = requests.get(url).json()
                try:
                    if len(presets[str(ctx.author.id)]) >= 2:
                        return await ctx.message.reply(messages.rate_limit)
                    
                    presets[str(ctx.author.id)][guild.id] = {
                        "name": "default",
                        "hide": False,
                        "lock": False,
                        "members": [],
                        "admins": [],
                        "blocks": []
                    }
                except KeyError:
                    presets[str(ctx.author.id)] = {
                        guild.id: {
                        "name": "default",
                        "hide": False,
                        "lock": False,
                        "members": [],
                        "admins": [],
                        "blocks": []
                        }
                    }

                headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
                new_data = json.dumps(presets)
                requests.put(url, headers=headers, data=new_data)
                await utils.send_presets(self.client)
                await send_configs()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        preset_ = None
        url = f'https://jsonstorage.net/api/items/{getenv("Presets")}'
        presets = requests.get(url).json()
        for preset in presets:
            try:
                preset_ = presets[preset][str(guild.id)]
                presets.pop(preset) if preset_ and len(presets) == 1 else presets[preset].pop(preset_)
            except KeyError:
                pass

        if preset_:
            headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
            new_data = json.dumps(presets)
            requests.put(url, headers=headers, data=new_data)
            await utils.send_presets(self.client)
             

def setup(client):
    client.add_cog(TRConfig(client))