import tkinter as tk
import moviepy.editor as mp

root = tk.Tk()

files=input("Enter path to mp4 : ")
def videoToAudio(videos):
    # Taking video file
    clip=mp.VideoFileClip(videos)
    # Asking if to trim using TKINTER
    ask=str(input("Want to trim ? (Y/N)")).lower()[0]
    if ask=='y':
        start=int(input("Enter starting value (in sec) : "))
        end=int(input("Enter ending value (in sec) : "))
        sbClip=clip.subclip(start,end)
        sbClip.audio.write_audiofile("audio.mp3")
    elif ask=='n':
        clip.audio.write_audiofile("audio.mp3")
    else:
        print('Error ! Please specify Y/N')





videoToAudio(files)

