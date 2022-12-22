from pytube import YouTube

link = input("Put your youtube link here!!! URL:")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()

video.download()

print("Download has completed!!")


