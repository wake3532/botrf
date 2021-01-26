import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = [" 봇 점검자 : 🌸 LYZE 🌸#2021  ", "봇 에러 발생시 🌸 LYZE 🌸#2021한테 디엠 부탁드려요" , " 봇 호스팅 상태 : ㄱㅊ "]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_member_join(member):
    embed=discord.Embed(title="<:4114110118_pandaclipartemojipand:798106315716952074> 익명님이 입장하셧습니다. 환영해요!")
    embed.set_image(url="https://media.discordapp.net/attachments/760040615781072946/803580701819142184/banner.gif")
    await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
