import requests
import discord
from discord.ext import commands
from os import getenv
import dotenv

class LolProfile(commands.Cog):
    def __init__(self, client):
        self.client = client
        dotenv.load_dotenv(dotenv.find_dotenv())

    @commands.command()
    async def lolprofile(self, ctx, server, *, username):
        summoner = requests.get(f'https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={getenv("RGKEY")}').json()
        summoner_icon = f'http://ddragon.leagueoflegends.com/cdn/11.17.1/img/profileicon/{summoner["profileIconId"]}.png'
        ranked_stats = requests.get(f'https://{server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner["id"]}?api_key={getenv("RGKEY")}').json()
        embed = discord.Embed(title=f'League Profile: {summoner["name"]}', color=0x2f3136)
        embed.add_field(name='Level/Region:', value=f'{summoner["summonerLevel"]} / BR', inline=True)
        embed.add_field(name='Last Games:', value='10W 0D / 100%WR', inline=True)
        yuumi = self.client.get_emoji(885499285502853200)
        katarina = self.client.get_emoji(885498652590759986)
        syndra = self.client.get_emoji(885498626892242994)
        m7 = self.client.get_emoji(885500263878770738)
        m6 = self.client.get_emoji(885501742958149632)
        embed.add_field(name='Top mastery champions:', value=f'''{yuumi} {m7} Yuumi **-** 1.098.876
        {syndra} {m7} Syndra **-** 876.245
        {katarina} {m6} Katarina **-** 3.671.356''', inline=False)
        if len(ranked_stats) == 0:
            pass
        if len(ranked_stats) == 1:
            print('test')
        if len(ranked_stats) == 2:
            soloq_tier = self.client.get_emoji(860341434702626826)
            flex_tier = self.client.get_emoji(860341434841169940)
            embed.add_field(name='**Soloq Stats:**', value=f'''{soloq_tier} **Platinum II**
            Rank: **1** (BR: 1)
            Top 0,0000001%

            League Points: **100LP**
            Wins: **100** **/** Defeats: **0**
            Winrate: **100%**''', inline=True)
            embed.add_field(name='**Flex Stats:**', value=f'''{flex_tier} **Challenger**
            Rank: **1** (BR: 1)
            Top 0,0000001%

            League Points: **1970LP**
            Wins: **100** **/** Defeats: **0**
            Winrate: **100%**''', inline=True)
        embed.add_field(name='Last game:', value='')
        embed.set_thumbnail(url=summoner_icon)
        await ctx.message.reply(embed=embed)

def setup(client):
    client.add_cog(LolProfile(client))