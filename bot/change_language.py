import discord
from discord.ext import commands
import json
import utils
import requests
import dotenv
from os import getenv

class Language(commands.Cog):
    def __init__(self, client):
        self.client = client
        dotenv.load_dotenv(dotenv.find_dotenv())
    
    @commands.command(aliases=['changelanguage', 'setlanguage', 'idioma', 'lingua'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def language(self, ctx):
        embed=discord.Embed(title=f"Selecionar idioma", description = """Altere meu idioma reagindo ao emoji correspondente 
        à língua que deseja.
        
        **Linguagens disponíveis:**""",  color=0x2f3136)
        embed.add_field(value=':flag_br:  Português', name=f'ㅤ', inline=True)
        embed.add_field(value=':flag_us:  Inglês', name=f'ㅤ', inline=True)
        embed.add_field(value=':flag_es:  Espanhol', name=f'ㅤ', inline=True)
        embed.set_footer(text='Quer me ajudar a traduzir para novas línguas? Entre no meu servidor:')
        message = await ctx.send(embed=embed)
        await message.add_reaction('🇧🇷')
        await message.add_reaction('🇺🇸')
        await message.add_reaction('🇪🇸')
        def check(reaction, user):
            return user == ctx.author and reaction.emoji and reaction.message.id == message.id
        reaction, _user = await self.client.wait_for("reaction_add", timeout=60.0,  check=check)
        if reaction.emoji == str('🇧🇷'):
            idioma, language = 'Português', 'portuguese'

        if reaction.emoji == str('🇺🇸'):
            idioma, language = 'Inglês', 'english'
        
        if reaction.emoji == str('🇪🇸'):
            idioma, language = 'Espanhol', 'spanish'

        url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        data = requests.get(url).json()
        data[str(ctx.guild.id)]["language"] = language
        new_data = json.dumps(data)
        requests.put(url, headers=headers, data=new_data)

        await ctx.message.reply(f'{ctx.author.mention}, você alterou meu idioma para `{idioma}`!')
        await utils.send_configs(self.client)
        
        
def setup(client):
    client.add_cog(Language(client))