import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from utils import Config

class NameMc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def namemc(self, ctx):
        await ctx.message.reply('Devido à atualizações recentes no site do NameMC, estou com problemas para requisitar os dados do site, o comando vai ficar sem funcionar por um tempo, infelizmente :/')
    
def setup(client):
    client.add_cog(NameMc(client))