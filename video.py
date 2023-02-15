from tkinter import *
from tkVideoPlayer import TkinterVideo
from datetime import *

video =Tk()
video.geometry("1000x600")
video.title("ZETA CORE")
photo = PhotoImage(file = r"ICONS\Zeta.png")
video.iconphoto(False, photo)
video.resizable(False, False)

videoplayer = TkinterVideo(master=video, scaled=True)
videoplayer.load(r"VIDEOS\ZETACORE.mp4")
videoplayer.set_size(size=(1000, 600), keep_aspect=False)
videoplayer.pack(expand=True, fill="both")
videoplayer.play()


def video_ended(event):
    # print("video ended")
    
    duration_video = videoplayer.current_duration()
    # print(f"video duration: {duration_video}")
    if(duration_video == 14.833333333333334):
        video.destroy()
videoplayer.bind("<<Ended>>", video_ended )

video.mainloop()