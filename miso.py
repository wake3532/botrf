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
        messages = ["제 접두사는 * 입니다!", "∑」FOR#1234님이 제작했어요!" , "TEAM MB" , str(user) + "분이 제 봇을 이용중입니다.", str(server) + "개의 서버에 있습니다."]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention} 님이 서버에 입장하셨습니다. ")
    except:
        pass

@client.event
async def on_member_remove(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(member.name + "님이  ``" + member.guild.name + "`` 서버에서 나가셨습니다 ")
    except:
        pass

@client.event
async def on_message(message)
    if message.content.startswith("*핑"):
        la = client.latency
        embed = discord.Embed(title="퐁!")
        embed.add_field(name="반응 속도", value=str(round(la * 1000)) + "ms")
        embed.set_footer(text=message.author.name + " | Sky BOT#2208  스카이봇은 2명이 개발하고 있어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('*정보'):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
        roles=[role for role in user.roles]
        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
        embed.set_author(name=f"{user}님의 정보!")
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

    if (message.content.split(" ")[0] == "*밴"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 서버 추방", description=f'당신은 **{message.guild.name}** 서버에서 차단되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Ban Success", description=f"{message.author.mention} 님, 성공적으로 차단시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.", color=0xff0000))
            return


    if message.content == '*서버정보':
        rnrrk = message.guild.region
        print(message.guild.region)
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"{message.guild.name}")
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
        embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
        embed.add_field(name="서버 국가", value=rnrrk, inline=False)
        embed.add_field(name="서버 Owner", value=f'<@{message.guild.owner.id}>', inline=False)
        embed.add_field(name="서버 Owner ID", value=message.guild.owner.id, inline=False)
        embed.add_field(name="서버 멤버 수", value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)', inline=False)
        embed.add_field(name="서버 채널 수", value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)', inline=False)
        embed.add_field(name="서버 부스트 레벨", value=f'{message.guild.premium_tier}레벨', inline=False)
        embed.add_field(name="서버 부스트 횟수", value=f'{message.guild.premium_subscription_count}번', inline=False)
        if message.guild.afk_channel != None:
            embed.add_field(name = f'잠수 채널', value = f'<#{message.guild.afk_channel.id}> \n ( 시간 제한 : {message.guild.afk_timeout} 초 )', inline = False)
        else:
            embed.add_field(name="잠수 채널", value="잠수 채널이 없습니다.")
        if message.guild.system_channel != None:
            embed.add_field(name = f'시스템 채널', value = f'<#{message.guild.system_channel.id}>', inline = False)
        else:
            embed.add_field(name="잠수 채널", value="시스템 채널이 없습니다.")
        embed.set_footer(text=f"{message.author}, 인증됨 | 준홍봇의 코드를 참고했어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("*계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                if calcResult < 1000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 더하기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 1000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 더하기 결과 ", description="계산 결과가 [ 1, 000, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 빼기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 빼기 결과 ", description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                if calcResult < 10000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 곱하기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 10000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 곱하기 결과 ", description="계산 결과가 [ 10, 000, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 나누기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 나누기 결과 ", description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
        except IndexError:
            embed = discord.Embed(title="SkyBOT : 계산 오류", description="2개의 숫자가 포함되지 않았어요!", timestamp=message.created_at,
            colour = discord.Colour.dark_red()        
        )
            await message.channel.send(embed=embed)
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")


    if message.content == '*명령어':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="보내는중..", value=":yes: 잠시 기다려 주세요", inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                time.sleep(3)
                await message.delete()
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name=":wave: 안녕하세요! 명령어들 앞에는 JELLO PRO 라는 칭호가 붙어요! 지금부터 도움말 들어옵니다!", value="도움말 시작!", inline=True)
                embed.add_field(name="도움말 1", value="*킥 *밴 *청소 *실검 *계산 *서버정보 *정보 *핑", inline=True)
                embed.add_field(name="도움말 2", value="준비중이에요!", inline=True)
                await message.channel.send(embed=embed)


    if (message.content.split(" ")[0] == "*킥"):
        if (message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 서버 추방", description=f'당신은 **{message.guild.name}** 서버에서 추방되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Kick Success", description=f"{message.author.mention} 님, 성공적으로 추방시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 추방할 수 있는 권한이 없습니다.", color=0xff0000))
            return 

    if message.content == "*실검":
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위 | "+e.text+"\n"
        await message.channel.send(result)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
