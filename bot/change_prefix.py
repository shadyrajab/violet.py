import discord
from discord.ext import commands
import json
import utils
import requests
from translates import changeprefix, prefix_limit
import dotenv
from os import getenv

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
        dotenv.load_dotenv(dotenv.find_dotenv())
    
    @commands.command(aliases=['changeprefix', 'setprefix'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def prefix(self, ctx, prefix):
        language = utils.Config(ctx.guild).language
        if len(prefix) > 3:
            return ctx.message.reply(prefix_limit(language))
        url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
        headers = {'Content-Type': "application/json; charset=utf-8",'dataType': "json"}
        data = requests.get(url).json()
        data[str(ctx.guild.id)]["prefix"] = prefix
        new_data = json.dumps(data)
        requests.put(url, headers=headers, data=new_data)
        await ctx.message.reply(changeprefix(language=language, prefix=prefix))
        await utils.send_configs(self.client)


def setup(client):
    client.add_cog(Prefix(client))