from tkinter import *
from tkVideoPlayer import TkinterVideo
from datetime import *

root =Tk()
root.geometry("1500x900")
def video_ended():
    print("endded")

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"VIDEOS\ZETACORE.mp4")
videoplayer.set_size(size=(1000, 600), keep_aspect=False)
videoplayer.pack(expand=True, fill="both")
videoplayer.play()
def video_ended(event):
    duration_video = videoplayer.current_duration()
    if(duration_video == 9.916666666666666):
        root.destroy()

videoplayer.bind("<<Ended>>", video_ended )
root.mainloop()