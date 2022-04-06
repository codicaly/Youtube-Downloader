from pytube import YouTube

print("Youtube Downloader")
link = input("Enter the youtube video Link : ")
path = input("Enter Where you want to download : ")

try:
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True).get_highest_resolution()
    stream.download(path)
    print("Download Completed....")
except:
    print("Some Error !! Can't Download..... Sorry")
