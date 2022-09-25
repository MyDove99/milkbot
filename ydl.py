#ydl.py
import youtube_dl #youtube_dl

def ydl(url):
    ydl_opts = { #다운로드 옵션
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        'outtmpl': 'song.mp3', #파일 이름
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) #다운로드
