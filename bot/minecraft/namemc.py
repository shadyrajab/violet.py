import discord
from discord import embeds
from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import datetime
from utils import Config
import json
import requests
import datetime

class NameMc(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def namemc(self, ctx, username):
        def EnviarRequestGet(url):
            return requests.get(url)

        def RetornarData(timestamp):
            return str(datetime.datetime.fromtimestamp(int(str(timestamp)[0:10])))[0:10].replace('-', '/')

        def RetornarHora(timestamp):
            return str(datetime.datetime.fromtimestamp(int(str(timestamp)[0:10])))[10:19]

        def GradeHead(username, embed):
            comando = "`1.13+`\n/give @p minecraft:player_head{SkullOwner:\"%s\"}" % username + "\n  `1.12-`\n/give @p minecraft:skull 1 3 {SkullOwner:\"%s\"}" % username   
            embed.add_field(name="Comando para obter a cabeça", value=comando, inline=False)

        def GradeDoUsuario(infoDoJogador, embed):
            mensagem = ""
            dataModificacao = ""
            horaModificacao = ""

            for i in infoDoJogador:
                mensagem += "``%s``" % (infoDoJogador.index(i) + 1) + "-" + "%s" % i['name'] + "\n"        

                if(infoDoJogador.index(i) == 0):
                    dataModificacao += "Nome Original\n"
                    horaModificacao += "\u200B \n"
                else:
                    dataModificacao += RetornarData(i['changedToAt']) + "\n"
                    horaModificacao += RetornarHora(i['changedToAt']) + "\n"

            embed.add_field(name="Histórico de nomes", value=mensagem, inline=True)
            embed.add_field(name='\u200B', value=dataModificacao, inline=True)
            embed.add_field(name='\u200B', value=horaModificacao, inline=True)
        
        def CriarEmbed(infoDoJogador, uuid, username):
            embed = discord.Embed(colour=discord.Colour(0x9013fe), description="Clique aqui para ver o perfil no [NameMc](https://pt.namemc.com/profile/%s)" % username)
            embed.set_thumbnail(url="https://crafatar.com/renders/body/%s" % uuid)
            embed.set_author(name="Histórico do jogador %s" % username, icon_url="https://crafatar.com/renders/head/%s" % uuid)
            embed.add_field(name="UUID", value=uuid, inline=False)
            embed.add_field(name="Skin", value="[Ver Skin](https://crafatar.com/renders/body/%s)" % uuid, inline=False)

            GradeDoUsuario(infoDoJogador, embed)

            GradeHead(username, embed)

            return embed

        try:
            uuid = json.loads(EnviarRequestGet("https://api.mojang.com/users/profiles/minecraft/%s" % username).text)['id']
            infoDoJogador = json.loads(EnviarRequestGet("https://api.mojang.com/user/profiles/%s/names" % uuid).text)

            embed = CriarEmbed(infoDoJogador, uuid, username)
            await ctx.message.reply(embed=embed)
        except Exception:
            await ctx.message.reply("Não foi possível encontrar o usuário %s" % username)


def setup(client):
    client.add_cog(NameMc(client))