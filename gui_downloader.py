from tkinter import *
import time
from pytube import YouTube
# PIL = python image library
# newer version of pil is pillow
# from PIL import ImageTk, Image
global video_title
global streams_pixel
global streams_itag
global var
global yt


root = Tk()
# window title
root.title("Downloader")
root.geometry("500x500")
root.iconbitmap("source/yang.ico")


def download():
    download_video = yt.streams.get_highest_resolution()
    download_video.download("/source")


def video_resolution():
    global var

    quality_options = []
    var = StringVar()
    # setting default value
    var.set("Quality")
    for quality in streams_pixel:
        quality_options.append(quality)
    label_title = Label(root, text=video_title, border=2)
    label_title.pack(pady=3)
    drop = OptionMenu(root, var, *quality_options)
    drop.pack()
    button_download = Button(root, text="Download", command=download).pack(pady=5)


def video_link():
    global streams_pixel
    global video_title
    global yt
    global streams_itag
    streams = []
    streams_pixel = []
    streams_itag = []

    # taking youtube video link
    link = url_entry.get()

    # starting Youtube with the link
    # It will help us reveal all the information about the video
    # link: https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=RDkJQP7kiw5Fk&start_radio=1
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True)
    # stream_sound = yt.streams.filter(only_audio=True)
    for stream in stream:
        streams.append(str(stream))
    # for stream in stream_sound:
    #     streams.append(stream)
    for itag in streams:
        result = itag.find('itag')
        quality = itag[result + 6:result + 9]
        quality = quality.replace('"', '')
        quality = quality.replace(" ", "")
        streams_itag.append(quality)


    for word in streams:
        result = word.find('res')
        quality = word[result + 5:result + 10]
        quality = quality.replace('"', '')
        streams_pixel.append(quality)

    # print(streams_pixel)
    # Title of video
    video_title = yt.title
    print("Title: ", video_title)

    video_resolution()


welcome_label = Label(root, text="welcome to Youtube Downloader", font=('Arial', 25))
welcome_label.pack(pady=10)

url_text = Label(root, text="Paste youtube URL below").pack(pady=10)

url_entry = Entry(root, textvariable="url Link", font=('calibre', 10, 'normal'), width=50)
url_entry.pack(pady=10)


button_send_link = Button(root, text="enter", command=video_link).pack(pady=10)
# window icon.. you need to put the path


root.mainloop()
