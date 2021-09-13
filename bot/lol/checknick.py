import discord
from discord.ext import commands
import requests
from datetime import date, datetime
from os import getenv
import dotenv

class CheckNick(commands.Cog):
    def __init__(self, client):
        self.client = client
        dotenv.load_dotenv(dotenv.find_dotenv())

    @commands.command()
    async def lolchecknick(self, ctx, server, *, username):
        summoner = requests.get(f'https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={getenv("RGKEY")}').json()
        matchs = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner["puuid"]}/ids?start=0&count=20&api_key={getenv("RGKEY")}').json()
        last_match = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{matchs[0]}?api_key={getenv("RGKEY")}').json()
        data = datetime.fromtimestamp(last_match["info"]["gameStartTimestamp"] / 1e3)
        disponibility = str(datetime.now() - data).split()
        disponibility = 910 if not 'days,' in disponibility and not 'day,' in disponibility else 910 - int(disponibility[0])
        print(disponibility)

def setup(client):
    client.add_cog(CheckNick(client))