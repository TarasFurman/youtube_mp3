import youtube_dl
import os
from sys import argv

# Download data and conf

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

# Save directory
if not os.path.exists('Youtube'):
    os.mkdir('Youtube')
else:
    os.chdir('Youtube')

# Download sound
with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + argv[1], 'r') as f:
        for youtube_url in f:
            dl.download([youtube_url])
