from pytube import YouTube

def downloadYouTubeAudio(url):
    url = 'https://www.youtube.com/watch?v=9aULhzn37DE'
    yt = YouTube(url)
    streamList = yt.streams.filter(only_audio=True).all()
    streamList[0].download()