import tkinter as tk
import moviepy.editor as mp

root = tk.Tk()

files=input("Enter path to mp4 : ")
def videoToAudio(videos):
    # Taking video file
    clip=mp.VideoFileClip(videos)
    # Asking if to trim using TKINTER
    ask=str(input("Want to trim ? (Y/N)")).lower()[0]
    askName=input("What name you want to give to audio file ? ").lower()
    askExt=input("What type of audio file ? ").lower()
    if ask=='y':
        start=int(input("Enter starting value (in sec) : "))
        end=int(input("Enter ending value (in sec) : "))
        sbClip=clip.subclip(start,end)
        sbClip.audio.write_audiofile(askName + "." + askExt)
    elif ask=='n':
        clip.audio.write_audiofile(askName + "." + askExt)
    else:
        print('Error ! Please specify Y/N')






videoToAudio(files)

