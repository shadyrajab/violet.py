import discord
from discord.ext import commands
from datetime import datetime
import json
import requests

class NameMc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def namemc(self, ctx, username):
        try:
            user = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}').json()
        except :
            return await ctx.message.reply(f'Não foi possível encontrar o usuário de nick: {username}')
        history_name = requests.get(f'https://api.mojang.com/user/profiles/{user["id"]}/names').json()
        history_name.reverse()
        avatar = f'https://crafatar.com/avatars/{user["id"]}?overlay'
        skin = f'https://crafatar.com/skins/{user["id"]}'
        skin_render = f'https://crafatar.com/renders/body/{user["id"]}?overlay'
        data, data_ = '', ''
        embed = discord.Embed(colour=0x2f3136, description='Perfil de Minecraft:')
        embed.set_thumbnail(url=skin_render)
        embed.set_author(name=f'{user["name"]}', icon_url=avatar)
        embed.add_field(name='UUID', value=user["id"])
        embed.add_field(name='Skin', value=f'[Baixar Skin]({skin})', inline=False)
        embed.add_field(name='Histórico de nomes', value=f'\n'.join(f'**{i} - **' + name["name"].replace('_', '\_') for i, name in enumerate(history_name, start=1)))
        for timestamp in history_name:
            try:
                dtobject = datetime.fromtimestamp(int(str(timestamp["changedToAt"])[0:10]))
                data += dtobject.strftime('%d/%m/%Y') + '\n'
                data_ += dtobject.strftime('%H:%M:%S') + '\n'
            except:
                pass
        embed.add_field(name='\u200B', value=data)
        embed.add_field(name='\u200B', value=data_)
        embed.add_field(name='Comando para obter a cabeça', value="**1.13+**\n/give @p minecraft:player_head{SkullOwner:\"%s\"}" % user["name"] + "\n  **1.12-**\n/give @p minecraft:skull 1 3 {SkullOwner:\"%s\"}" % user["name"])
        embed.timestamp = datetime.now()
        await ctx.message.reply(embed=embed)

def setup(client):
    client.add_cog(NameMc(client))