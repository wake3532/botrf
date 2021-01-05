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
        messages = ["🌴 코로나 의심시 1339 ", "🎄 : cheerybot.com " , " 🌸 : 안녕하세요 " , str(user) + "분이 제 봇을 이용중입니다. 항상 고마워요! ", str(server) + "개의 서버에 있습니다. 저를 초대해 더 늘려주세요 ! ❤ "]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)


@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 입장',
            description=f'{member}님이{member.guild}서버에 입장 했습니다. 환영해요  [<:link:788705500060450838>봇초대](https://discord.com/api/oauth2/authorize?client_id=795856795297513482&permissions=8&scope=bot)\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None
@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 퇴장',
            description=f'{member}님이{member.guild}에 퇴장 했습니다. 잘가세요 ![<:link:788705500060450838>봇초대](https://discord.com/api/oauth2/authorize?client_id=795856795297513482&permissions=8&scope=bot)  \n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

@client.event
async def on_message(message):
    if message.content.startswith("c/ping"):
        la = client.latency
        embed = discord.Embed(title="<a:fwq:792379073292795944>  현재 핑 상태입니다.  [ 0.1초마다 핑 속도 업데이트중  ] ")
        embed.add_field(name="반응 속도", value=str(round(la * 1000)) + "ms")
        embed.set_footer(text=message.author.name + " 호스팅 부분에서 핑 속도에 문제가 있을 수 있어요.  ", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

        
    if message.content.startswith('c/info'):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
        roles=[role for role in user.roles]
        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
        embed.set_author(name=f"{user}님의 정보입니다 [<:warning:788704019852820491>  {user}님이 정보 가져오기를 별로 싫어하면 하지 말아주세요 ]  ")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"{message.author}님에 정보를 가져온겁니다.", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=user.id, inline = False)
        embed.add_field(name="닉네임", value=user.display_name, inline = False)
        embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=user.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =user.status, inline = False)
        await message.channel.send(embed=embed)

    if (message.content.split(" ")[0] == "c!ban"):
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="<a:fwq:792379073292795944>  곧 밴 됍니다 기다리세요  ", value="  최대한 빨리 처리해드릴게요 ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증안됌", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                time.sleep(8)
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="밴 돼셨습니다", description=f' <:warning:788704019852820491> 당신은 **{message.guild.name}** 서버에서 차단되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Ban Success", description=f"{message.author.mention} 님, 성공적으로 차단시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.", color=0xff0000))
            return

 
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
