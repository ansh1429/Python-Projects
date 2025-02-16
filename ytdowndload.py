from tkinter import *
from pytube import YouTube
from pytube import request
import ssl

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Add custom User-Agent header
request.default_headers["User-Agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

root = Tk()
lbl = Label(root, text="Enter YouTube link:")
lbl.pack()
inp = Entry(root)
inp.pack()


def fun():
    txt.delete("1.0", END)
    try:
        url = YouTube(str(inp.get()))
        video = url.streams.get_highest_resolution()
        video.download()
        txt.insert("1.0", "Downloading successful!")
    except Exception as e:
        txt.insert("1.0", f"Error: {str(e)}")


btn = Button(root, text="Click", command=fun)
btn.pack()
txt = Text(root, width=30, bg="skyblue", fg="black")
txt.pack()
root.mainloop()
