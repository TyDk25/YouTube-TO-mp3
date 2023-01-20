from pytube import YouTube
import os




def new_func(link):

    yt = YouTube(link)

    ys = yt.streams.filter(only_audio=True).first()

    out_file = ys.download('MP3 Version')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
# result of success
    print(f" The song {yt.title} has been downloaded successfully!")


