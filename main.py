from tkinter import *
from pytube import YouTube

#initalising tkinter
root = Tk()

# setting geometry of GUI
root.geometry("400x350")

# setting the title of GUI
root.title("YouTube Video Downloader Application")

# defining download function
def download():
    # using try and except to execute program without errors
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get().streams.first().download())
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

# create the label widget to welcome user
Label(root, text="Welcome to YouTube\nDownloader Application", font="Consolas 15 bold").pack()

# declaring StringVar type variable
myVar = StringVar()

# setting the default text to myVar
myVar.set("Enter the link below")

# created the Entry widget to ask user to enter the URL
Entry(root,textvariable=myVar, width=40).pack(pady=10)

# declaring StringVar type variable
link = StringVar()

# created the entry widget to get the link
Entry(root,textvariable=link, width=40).pack(pady=10)

# created and called the download function to download video
Button(root, text="Download Video", command=download).pack()

# running the mainloop
root.mainloop()

