import discord
import asyncio
from discord.ext import commands
import youtube_dl
import re
import pandas as pd
from bs4 import BeautifulSoup
import bs4
import urllib
import requests
import os
import random
from selenium import webdriver
import lxml
#from ydl import *

client = commands.Bot(command_prefix='!')
searchYoutube={}
searchYoutubeHref={} # 유튜브 하이퍼링크 모음
voice = None
url = ('')
urllist = ['','','','','']

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!명령어로 명령어를 확인하세요"))
    print("logged in as {0.user}".format(client))


@client.command()
async def 들어와(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        global voice
        channel = ctx.author.voice.channel
        voice = await channel.connect()
    
    else:
        await ctx.send("음성채널 없음")

@client.command()
async def 나가(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        global voice
        channel = ctx.author.voice.channel
        await client.voice_clients[0].disconnect()

    else:
        await ctx.send("나갈수 없음")

@client.command()
async def 노래틀어줘(ctx):
    global url
    if url== '':
        await ctx.send('주소가 없습니다')
    else :
        channel = ctx.author.voice.channel
        if client.voice_clients == []:
            await channel.connect()
            await ctx.send('노래를 재생합니다 :musical_note: ')

            if urllist[0] == '' and urllist[1] == '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
        
            elif urllist[0] != '' and urllist[1] == '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
                url =urllist[0]
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
                urllist[0] = None
            
            elif urllist[0] != None and urllist[1] != None and urllist[2] == None and urllist[3] == None and urllist[4] == None:
                url =urllist[0]
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
                urllist[0] = urllist[1]
                urllist[1] = ''
            
            
            
            elif urllist[0] != '' and urllist[1] != '' and urllist[2] != '' and urllist[3] == '' and urllist[4] == '':
                url =urllist[0]
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
                urllist[0] = urllist[1]
                urllist[1] = urllist[2]
                urllist[2] = ''
            
            elif urllist[0] != '' and urllist[1] != '' and urllist[2] != '' and urllist[3] != '' and urllist[4] == '':
                url =urllist[0]
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
                urllist[0] = urllist[1]
                urllist[1] = urllist[2]
                urllist[2] = urllist[3]
                urllist[3] = ''

            elif urllist[0] != '' and urllist[1] != '' and urllist[2] != '' and urllist[3] != '' and urllist[4] != '':
                url =urllist[0]
                ydl_opts = {'format': 'bestaudio'}
                FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']
                voice = client.voice_clients[0]
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                url=('')
                urllist[0] = urllist[1]
                urllist[1] = urllist[2]
                urllist[2] = urllist[3]
                urllist[3] = urllist[4]
                urllist[4] = ''

@client.command()
async def 노래예약(ctx):
    global url
    if url == '':
        await ctx.send('주소가 없습니다.')
    elif urllist[0] == '' and urllist[1] == '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
        urllist[0] = url
        await ctx.send('1번에 예약했습니다')
            
    elif urllist[0] != '' and urllist[1] == '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
        urllist[1] = url
        await ctx.send('2번에 예약했습니다')
            
    elif urllist[0] != '' and urllist[1] != '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
        urllist[2] = url
        await ctx.send('3번에 예약했습니다')
            
    elif urllist[0] != '' and urllist[1] != '' and urllist[2] != '' and urllist[3] == '' and urllist[4] == '':
        urllist[3] = url
        await ctx.send('4번에 예약했습니다')
            
    elif urllist[0] != '' and urllist[1] != '' and urllist[2] != '' and urllist[3] != '' and urllist[4] == '':
        urllist[4] = url
        await ctx.send('5번에 예약했습니다')
    else:
        await ctx.send('더이상 예약을 할 수 없습니다')

@client.command()
async def 예약리스트(ctx):
    if urllist[0] == '' and urllist[1] == '' and urllist[2] == '' and urllist[3] == '' and urllist[4] == '':
        await ctx.send('예약된게 없습니다.')
    else:
        await ctx.send('1번: '+urllist[0]+' 2번: '+urllist[1]+' 3번: '+urllist[2]+' 4번: '+urllist[3]+' 5번: '+urllist[4])

@client.command()
async def 노래멈춰(ctx):
    if not client.voice_clients[0].is_paused():
        client.voice_clients[0].pause()
        await ctx.send("노래를 멈춥니다")
    else:
        await ctx.send("노래가 재생중이지 않습니다")

@client.command()
async def 노래다시켜(ctx):
    if client.voice_clients[0].is_paused():
        client.voice_clients[0].resume()
        await ctx.send("노래를 재생합니다")
    else:
        await ctx.send("노래가 재생중이지 않습니다")
        
@client.command()
async def 노래꺼(ctx):
    if client.voice_clients[0].is_playing():
        client.voice_clients[0].stop()
        await ctx.send("노래를 끕니다")
        url=('')
    else:
        await ctx.send("노래가 재생중이지 않습니다")

@client.command()
async def 주소입력(ctx,youtube):
    global url
    if youtube != None:
        url = youtube
        await ctx.send(url+" 주소로 저장되었습니다")
    else :
        await ctx.send("주소입력에 주소가 없습니다.")

@client.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요")

@client.command()
async def 에어컨(ctx):
    await ctx.send("먹었어요")

@client.command()
async def 쭈꾸미(ctx):
    await ctx.send("존나 맛있다")

@client.command()
async def 주소(ctx):
    if url=='':
        await ctx.send('주소가 없습니다')
    else:
        await ctx.send(url)

@client.event
async def on_message(message):
    global url
    await client.process_commands(message)
    if message.author == client.user:
        return
    if message.content.startswith('!명령어'):
        embed=discord.Embed(title="명령어",  description='우유', color=0x00D8FF)
        embed.add_field(name="기본",value='명령어 / 들어와 / 나가 / 안녕 / 에어컨 / 쭈꾸미',inline=False)
        embed.add_field(name="기능",value='골라줘[하고싶은거] / 팀짜줘[팀원] / 전적검색[닉네임]',inline=False)
        embed.add_field(name="노래",value='검색 / 노래틀어줘 / 주소 / 1~4번 / 노래멈춰 / 노래다시켜 / 노래꺼 / 노래예약 / 예약리스트 / 주소입력[url]',inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!골라줘'):
        name = message.content[5:len(message.content)]
        await message.channel.send('생각중..')
        name2 = name.split()
        choiceList = random.choice(name2)
        await message.channel.send(choiceList)

    if message.content.startswith('!검색'):
        text = message.content[4:len(message.content)]
        
        await message.channel.send('오래 기다려주세요.')
        
        driver = webdriver.Chrome(r'C:\Users\hanmi\Desktop\;   ;\chromedriver_win32\chromedriver.exe')
        driver.get('https://www.youtube.com/results?search_query='+text)
        source = driver.page_source
        soup = BeautifulSoup(source,'lxml')
        entire = soup.find_all('a', {'id': 'video-title'})
        
        embed = discord.Embed(
        title=text,
        description="검색한 영상 결과",
        colour=discord.Color.blue())

        for i in range(0, 4):
            entireNum = entire[i]
            entireText = entireNum.text.strip()  # 영상제목
            test1 = entireNum.get('href')  # 하이퍼링크
            rink = 'https://www.youtube.com'+test1
           # embed.add_field(name=str(i+1)+'번째 영상',value=entireText + '\n링크 : '+rink)
            embed.add_field(name=str(i + 1) + '번째 영상', value='\n' + '[%s](<%s>)' % (entireText, rink),
                        inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다
            searchYoutubeHref[i] = rink
        await message.channel.send(embed=embed)

    if message.content.startswith('1번'):
        if not searchYoutubeHref: 
            await message.channel.send("검색한 영상이 없습니다")
        else:
            print(searchYoutubeHref[0])
            url = searchYoutubeHref[0]
            print(url)
            for i in range(0,4):
                del searchYoutubeHref[i] 
            await message.channel.send("1번영상 선택됨")
                                       
    if message.content.startswith('2번'):
        if not searchYoutubeHref: 
            await message.channel.send("검색한 영상이 없습니다")
        else:
            print(searchYoutubeHref[1])
            url = searchYoutubeHref[1]
            print(url)
            for i in range(0,4):
                del searchYoutubeHref[i] 
            await message.channel.send("2번영상 선택됨")

    if message.content.startswith('3번'):
        if not searchYoutubeHref:
            await message.channel.send("검색한 영상이 없습니다")
        else:
            print(searchYoutubeHref[2])
            url = searchYoutubeHref[2]
            print(url)
            
            await message.channel.send("3번영상 선택됨")

            for i in range(0,4):
                del searchYoutubeHref[i]

    if message.content.startswith('4번'):
        if not searchYoutubeHref:
            await message.channel.send("검색한 영상이 없습니다")
        else:
            print(searchYoutubeHref[3])
            url = searchYoutubeHref[3]
            print(url)
            
            await message.channel.send("4번영상 선택됨")

            for i in range(0,4):
                del searchYoutubeHref[i]


    if message.content.startswith('!팀짜줘'):
        member = message.content[5:len(message.content)]
        await message.channel.send('최적의 팀 연산중..')
        member2 = member.split()
        team1 = random.sample(member2,5)
        Setteam1 = set(team1)
        Setteam2 = set(member2)
        team2 = str(team1)
        team3 = str(Setteam2.difference(Setteam1))
        team3 = team3.replace('{','[')
        team3 = team3.replace('}',']')
        
        await message.channel.send('1팀 :'+team2)
        await message.channel.send('2팀 :'+team3)
        
    if message.content.startswith('!상대검색'):
        nick = message.content[6:len(message.content)]
        req = requests.get('https://blitz.gg/lol/live/kr/'+nick)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        tm1 = soup.find_all('p','class')
        
    if message.content.startswith('!전적검색'):
        nick = message.content[6:len(message.content)]
        await message.channel.send('한번에 하나만 해주세요')
        req = requests.get('https://www.op.gg/summoner/userName='+nick)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        up1 = soup.find_all('div','TierRankInfo')
        up2 = str(up1)
        if 'Unranked' in up2:
            embed=discord.Embed(title="롤 전적검색",  description=nick, color=0x00ff56)
            embed.set_thumbnail(url='https://opgg-static.akamaized.net/images/medals/default.png?image=q_auto:best&v=1')
            embed.add_field(name="랭크",value='언랭 점수: 0 LP',inline=False)
            embed.add_field(name="랭크",value="승리:0W 패배:0L 승률: 0%",inline=False)
            await message.channel.send(embed=embed)
            
        elif 'TierInfo' in up2:
            Rank1 = soup.find_all('div','TierRank')
            Rank2 = str(Rank1[0])[str(Rank1[0]).find('nk">')+4:str(Rank1[0]).find('</div>')]
            if 'master' in Rank2:
                LP1 = soup.find_all('span',{'class':'LeaguePoints'})
                LP2 = str(LP1[0])[str(LP1[0]).find('">')+4:str(LP1[0]).find('</span>')]
                LP3 = LP2.strip()

                win1 = soup.find_all('span',{'class':'wins'})
                win2 = str(win1[0])[str(win1[0]).find('">')+2:str(win1[0]).find('</span>')]

                lose1 = soup.find_all('span',{'class':'losses'})
                lose2 = str(lose1[0])[str(lose1[0]).find('">')+2:str(lose1[0]).find('</span>')]

                winratio1 = soup.find_all('span',{'class':'winratio'})
                winratio2 = str(winratio1[0])[str(winratio1[0]).find('Ratio')+5:str(winratio1[0]).find('</span>')]
                embed=discord.Embed(title="롤 전적검색",  description=nick, color=0x00ff56)
                embed.set_thumbnail(url='https://opgg-static.akamaized.net/images/medals/'+Rank2+'_1.png?image=q_auto&v=1')
                embed.add_field(name="랭크",value=Rank2+" 점수 :"+LP3,inline=False)
                embed.add_field(name="승률",value='승리:'+win2+' 패배:'+lose2+' 승률:'+winratio2,inline=False)
                await message.channel.send(embed=embed)
            elif 'Chall' in Rank2:
                LP1 = soup.find_all('span',{'class':'LeaguePoints'})
                LP2 = str(LP1[0])[str(LP1[0]).find('">')+4:str(LP1[0]).find('</span>')]
                LP3 = LP2.strip()

                win1 = soup.find_all('span',{'class':'wins'})
                win2 = str(win1[0])[str(win1[0]).find('">')+2:str(win1[0]).find('</span>')]

                lose1 = soup.find_all('span',{'class':'losses'})
                lose2 = str(lose1[0])[str(lose1[0]).find('">')+2:str(lose1[0]).find('</span>')]

                winratio1 = soup.find_all('span',{'class':'winratio'})
                winratio2 = str(winratio1[0])[str(winratio1[0]).find('Ratio')+5:str(winratio1[0]).find('</span>')]
                embed=discord.Embed(title="롤 전적검색",  description=nick, color=0x00ff56)
                embed.set_thumbnail(url='https://opgg-static.akamaized.net/images/medals/'+Rank2+'_1.png?image=q_auto&v=1')
                embed.add_field(name="랭크",value=Rank2+" 점수 :"+LP3,inline=False)
                embed.add_field(name="승률",value='승리:'+win2+' 패배:'+lose2+' 승률:'+winratio2,inline=False)
                await message.channel.send(embed=embed)
            else:
                Rank3 = Rank2[:-1].strip()
        
                LP1 = soup.find_all('span',{'class':'LeaguePoints'})
                LP2 = str(LP1[0])[str(LP1[0]).find('">')+4:str(LP1[0]).find('</span>')]
                LP3 = LP2.strip()

                win1 = soup.find_all('span',{'class':'wins'})
                win2 = str(win1[0])[str(win1[0]).find('">')+2:str(win1[0]).find('</span>')]

                lose1 = soup.find_all('span',{'class':'losses'})
                lose2 = str(lose1[0])[str(lose1[0]).find('">')+2:str(lose1[0]).find('</span>')]

                winratio1 = soup.find_all('span',{'class':'winratio'})
                winratio2 = str(winratio1[0])[str(winratio1[0]).find('Ratio')+5:str(winratio1[0]).find('</span>')]
                embed=discord.Embed(title="롤 전적검색",  description=nick, color=0x00ff56)
                embed.set_thumbnail(url='https://opgg-static.akamaized.net/images/medals/'+Rank3+'_1.png?image=q_auto&v=1')
                embed.add_field(name="랭크",value=Rank2+" 점수 :"+LP3,inline=False)
                embed.add_field(name="승률",value='승리:'+win2+' 패배:'+lose2+' 승률:'+winratio2,inline=False)
                await message.channel.send(embed=embed)
        else :
            await message.channel.send('찾을수 없는 유저입니다')

client.run('ODc1MzIyMTcyNzM2OTU4NTI0.YRT1TA.7lnsMxX4asK-Xh-yAszVMv-h_Mo')
