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

    if (message.content.split(" ")[0] == "?킥"):
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
                
    if message.content == "?help" or message.content == '?명령어':
        embed = discord.Embed(title="🎪ㅣJELLO 기본 명령어", timestamp=message.created_at, 
        colour=discord.Colour.dark_blue()    
    )
        embed.add_field(name="?명령어", value="명령어를 보여드려요!", inline=False)
        embed.add_field(name="?핑", value="퐁!", inline=False)
        embed.add_field(name="?청소 (수)", value="수 만큼 청소합니다.!", inline=False)
        embed.add_field(name="?서버정보", value="서버 정보를 보여드립니다!", inline=False)
        embed.add_field(name="?피드백 [ 내용 ]", value="피드백을 보내요!", inline=False)
        embed.add_field(name="?킥", value="서버에서 킥 합니다!", inline=False)
        embed.add_field(name="?다양한 말들", value="말에 답을 해드려요 하지만 거의 말을 못 할겁니다!", inline=False)
        embed.add_field(name="?공지", value="공지 메세지를 보내드려요! ㅣ 아 잠깐! 이 명령어는 관리 권환이 필요해요", inline=False)
        embed.set_footer(text="개발자는 ∑」FOR#1234 이에요!")
        await message.channel.send(embed=embed)
        
    if message.content == '?서버정보':
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
   
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
