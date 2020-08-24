import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from urllib.request import Request
from urllib import parse


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await message.channel.send(f"<@!{message.author.id}>좋은 한국어 인사 예절이네요 ! 보기 좋아요")

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

    if message.content.startswith("?피드백"):
        Dansdml1 = message.content[5:]
        Dansdml = discord.Embed(title="**[ JELLO BOT ]**", color=0x6777ff)
        Dansdml.add_field(name="• 문의하는 내용", value=f"{Dansdml1}\n\n• 문의하는 서버 : {message.guild.name}\n• 문의한 이용자 : {message.author.mention}", inline=False)
        Dansdml.set_thumbnail(url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
        Dansdml.set_footer(text=message.author.name + " | 이 내용이 전해집니다 스팸 메세지는 봇 제한이 될 수 있습니다. !", icon_url=message.author.avatar_url)
        m = await message.channel.send("문의발송 여부를 선택하여주세요.", embed=Dansdml)
        await m.add_reaction('✅')
        await m.add_reaction('❎')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
        except asyncio.TimeoutError:
            Drhdwltlrks = discord.Embed(title="**[ ERROR ]**", color=0xff0000)
            Drhdwltlrks.add_field(name="**문의**", value=f"{message.author.mention} **님 다른 사람이랑 대화 또는 너무 길게 피드백을 작성을 인식했어요 다시 시도 하십시오.**", inline=False)
            Drhdwltlrks.set_thumbnail(url=message.author.avatar_url)
            Drhdwltlrks.set_footer(text="∑」FOR#1234  | 피드백 코드의 원본은 djs226587#1243 님의 코드에요 !" , icon_url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
            await m.edit(content="문의발송이 취소되었습니다.", embed=Drhdwltlrks)
        else:
            if str(reaction.emoji) == "❎":
                Drhdwlcnlth = discord.Embed(title="**[ JELLO BOT ]**", color=0xff0000)
                Drhdwlcnlth.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송이 취소되었습니다.**", inline=False)
                Drhdwlcnlth.set_thumbnail(url=message.author.avatar_url)
                Drhdwlcnlth.set_footer(text="∑」FOR#1234 | 문의 발송이 취소되었습니다!" , icon_url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
                await m.edit(embed=Drhdwlcnlth)
            elif str(reaction.emoji) == "✅":
                await m.edit(content="서포트 서버에 피드백이 발송되었어요!", embed=Dansdml)
                await client.get_channel(int(737624237925466154)).send(embed=Dansdml)

                
    if message.content.startswith("?dm"):
        userdm = message.content[4:].split(",")
        getuser = userdm[0]
        getuserid = getuser[3:21]
        getusermention = client.get_user(int(getuserid))
        userdes = userdm[1]
        await getusermention.send(userdes)
        await message.channel.send("DM이 성공적으로 발송되었어요!")

    if message.content.startswith("?공지"):
            if message.author.id in owner:
                if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                    await message.channel.send("메세지를 쓰세요.")
                try:
                    msg = message.content[4:]
                    oksv = 0
                    embed = discord.Embed(
                        title = msg.split('&&')[0],
                        description = msg.split('&&')[1] + f"\n \n[서포트 서버](https://discord.gg/g5cEJzk)",
                        colour = discord.Colour.gold(),
                        timestamp = message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - Developer | 봇 공지는 기본적으로 랜덤 채널에 발송돼요! 자세한 설명은 /공지채널!') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                except IndexError:
                    await message.channel.send("형식이 틀렸습니다. ``*공지 <제목>&&<내용>``으로 다시 시도해보세요.")
                m = await message.channel.send("아래와 같이 공지가 발신됩니다.", embed=embed)
                await m.add_reaction('✅')
                await m.add_reaction('❎')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다.')
                else:
                    if str(reaction.emoji) == "❎":
                        await message.channel.send("공지발신을 취소하였어요")
                    elif str(reaction.emoji) == "✅":
                        await m.edit(content="발신중입니다...", embed=embed)
                        for i in client.guilds:
                            arr = [0]
                            alla = 거짓
                            국기 = True
                            z = 0
                            for j in i.channels:
                                arr.append(j.id)
                                z+=1
                                if "SkyBOT-공지" in j.name or"봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "테스트1" in j.name:
                                    if str(j.type)=='text':
                                        try:
                                            oksv += 1
                                            await j.send(embed=embed)
                                            alla = True
                                        except:
                                            패스
                                        깨다
                            if alla==False:
                                try:
                                    chan=i.channels[1]
                                except:
                                    패스
                                if str(chan.type)=='text':
                                    try:
                                        oksv += 1
                                        await chan.send(embed=embed)
                                    except:
                                        패스
                        await message.channel.send(f"**📢 공지 가 성공적으로 발신되었습니다. 📢**\n\n{len(client.guilds)}개의 서버 중에서  {oksv}개의 서버에 발신 완료했습니다., {len(client.guilds) - oksv}개의 서버에 발신 실패했습니다.")
                        await m.edit(content="발신이 완료되었습니다!", embed=embed)
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')

    if message.content.startswith("?청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[4:]
                await message.channel.purge(limit=int(amount))
                embed = discord.Embed(title="청소 완료!", description=f"{message.author.mention}, **{amount}** 개의 메시지를 청소했어요!", timestamp=message.created_at,
                colour = discord.Colour.green()
    )
                embed.set_footer(text="∑」FOR#1234", icon_url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
                await message.channel.send(embed=embed)
            except ValueError:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소할 메시지가 정해져 있지 않아요!", timestamp=message.created_at, 
                colour=discord.Colour.orange()
    )
                embed.set_footer(text="∑」FOR#1234", icon_url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
                await message.channel.send(embed=embed)
        else:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소를 실행할 권한이 부족해요!", timestamp=message.created_at, 
                colour=discord.Colour.red()
    )
                embed.set_footer(text="∑」FOR#1234", icon_url="https://cdn.discordapp.com/avatars/726974969661358140/4bd1945a3f76966b884077d9399fd560.png?size=256")
                await message.channel.send(embed=embed)



client.run('NzI2OTc0OTY5NjYxMzU4MTQw.XvlGMw.0M-nCRAbJR0tf47RpXAX0B-aIXg')
