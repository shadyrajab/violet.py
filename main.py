import discord
from discord.ext import commands 
import json
from os import walk, getenv
import utils
from utils import Config
import requests
from datetime import datetime
import random
import dotenv

def get_prefix(client, message):
    if isinstance(message.channel, discord.DMChannel):
        return ''
    config = Config(message.guild)
    return config.prefix

intents = discord.Intents.default()
intents.members = True
client = commands.AutoShardedBot(command_prefix=get_prefix, help_command=None, intents=intents)
dotenv.load_dotenv(dotenv.find_dotenv())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    print(f'{client.user.name} está online!')

@client.event
async def on_guild_join(guild):
    url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
    data = requests.get(url).json()
    data[str(guild.id)]= {
        'prefix': "*",
        'language': "portuguese" if str(guild.region) == 'brazil' else "english",
        'category_id': None,
        'channel_id': None
    }
    headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
    new_data = json.dumps(data)
    requests.put(url, headers=headers, data=new_data)
    await utils.send_configs(client)
    embed = discord.Embed(color=0x2f3136)
    bot = await client.fetch_user(705474553983533178)
    embed.set_author(name='Obrigada por me convidar!', icon_url=bot.avatar_url)
    embed.add_field(name='ㅤ', value='''**-** Use `*help` para ver a lista de comandos!
    **-** Altere meu prefixo com o comando `*changeprefix <prefix>`!
    **-** Ative o sistema de salas temporárias, use `*trsetup`!
    **-** Também posso falar outras línguas, mude meu idioma usando `*language`!
    
    💸 **Me ajude a me manter online, faça uma doação [clicando aqui](https://www.paypal.com/donate?hosted_button_id=4KQY6N6GC23RS)!**''')
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='Violet')
    channel = random.choice(guild.text_channels)
    await channel.send(embed=embed)
    cloud = client.get_guild(836748124139552788)
    logs = cloud.get_channel(851628704551534603)
    members = len(await client.fetch_guilds().flatten())
    await logs.send(f'Entrei no servidor **{guild.name}**, com **{guild.member_count} membros**. Agora estou em **{members} servidores.**')

@client.event
async def on_guild_remove(guild):
    url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
    data = requests.get(url).json()
    data.pop(str(guild.id))
    headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
    new_data = json.dumps(data)
    requests.put(url, headers=headers, data=new_data)
    await utils.send_configs(client)
    cloud = client.get_guild(836748124139552788)
    logs = cloud.get_channel(851628704551534603)
    members = len(await client.fetch_guilds().flatten())
    await logs.send(f'Saí do servidor **{guild.name}**, com **{guild.member_count} membros**. Agora estou em **{members} servidores.**')

@commands.Cog.listener()
async def on_message(message):
    if message.system_content == '<@!705474553983533178>': 
        config = Config(str(message.guild.id))
        await message.reply(f"Olá, meu prefixo aqui é `{config.prefix}`")

if __name__ == "__main__":
    for p, _, files in walk('bot'):
        for file in files:
            if '.pyc' in file or '.json' in file:
                continue
            client.load_extension(f"{p}.{file}".replace('\\', '.').replace('.py', ''))

    client.run(getenv("Violet"))