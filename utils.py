import discord
import re
import json
from datetime import datetime, timedelta
import requests
import dotenv
from os import getenv

dotenv.load_dotenv(dotenv.find_dotenv())
async def send_configs(client: discord.Client):
    cloud = client.get_guild(836748124139552788)
    data_channel = cloud.get_channel(836797802389831701)
    url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
    configs = requests.get(url).json()
    with open('config.json', 'w') as f:
        json.dump(configs, f, indent=4)

    file = discord.File('config.json')
    await data_channel.send(file=file)

async def send_presets(client: discord.Client):
    cloud = client.get_guild(836748124139552788)
    data_channel = cloud.get_channel(836797825026883606)
    url = f'https://jsonstorage.net/api/items/{getenv("Presets")}'
    configs = requests.get(url).json()
    with open('bot/temporaryrooms/presets.json', 'w') as f:
        json.dump(configs, f, indent=4)

    file = discord.File('bot/temporaryrooms/presets.json')
    await data_channel.send(file=file)

class Config():
    def __init__(self, guild):
        self.guild = guild
        self.url = f'https://jsonstorage.net/api/items/{getenv("Config")}'
        self.config = requests.get(self.url).json()

    @property
    def prefix(self):
        prefix = self.config[str(self.guild.id)]["prefix"]
        return prefix

    @property
    def language(self):
        if not self.guild:
            return 'portuguese'
        language = self.config[str(self.guild.id)]["language"]
        return language

    @property
    def channel_id(self):
        channel_id = self.config[str(self.guild.id)]["channel_id"]
        return channel_id

    @property
    def category_id(self):
        category_id = self.config[str(self.guild.id)]["category_id"]
        return category_id

def convert_to_seconds(time):
    days_, hours_, minutes_, seconds_ = 0, 0, 0, 0
    days = re.search(r'...d|..d|.d', time.lower())
    hours = re.search(r'...h|..h|.h', time.lower())
    minutes = re.search(r'...m|..m|.m', time.lower())
    seconds = re.search(r'...s|..s|.s', time.lower())
    if days:
        days = days.group()
        days = re.sub(r'[^0-9]', '', days)
        days_ = int(days) * 86400
    if hours:
        hours = hours.group()
        hours = re.sub(r'[^0-9]', '', hours)
        hours_ = int(hours) * 3600
    if minutes:
        minutes = minutes.group()
        minutes = re.sub(r'[^0-9]', '', minutes)
        minutes_ = int(minutes) * 60
    if seconds:
        seconds = seconds.group()
        seconds_ = re.sub(r'[^0-9]', '', seconds)
    
    return days_ + hours_ + minutes_ + int(seconds_)

def convert_to_time(segundos):
    horas = segundos // 3600
    dias = horas//86400

    segs_restantes = segundos % 3600
    minutos = segs_restantes // 60
    segs_restantes_final = segs_restantes % 60

    if horas >= 24: 
        dias = int(horas / 24)
        horas = int(horas % 24)

    tempo = []
    if dias:
        tempo.append(str(dias) + 'd')
    if horas:
        tempo.append(str(horas) + 'h')
    if minutos:
        tempo.append(str(minutos) + 'm')
    if segs_restantes_final:
        tempo.append(str(segs_restantes_final) + 's')

    return ', '.join(tempo), dias, horas, minutos, segs_restantes_final

def new_data(secs):
    date = convert_to_time(secs)
    days, hours, minutes, seconds = date[1], date[2], date[3], date[4]
    new_data = datetime.today() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return int(str(new_data)[0:19].replace('-', '').replace(':', '').replace(' ', ''))