import pygame
import tkinter as tk

root=tk.Tk()

n=int(input("How many songs you want to add : "))
musicArr=[]

def addInPlaylist(a):
    for i in range(1,a+1):
        files=input("Enter the file path / name : ")
        if files!='':
            musicArr.append(files + '.mp3')
        else:
            print("Error")
    for song in musicArr:
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(0)
            controller() 


# def playing():
def pause():
    pygame.mixer.music.pause()
    print("paused")

def resumed():
    pygame.mixer.music.unpause()
    print("playing")

def stopped():
    pygame.mixer.music.stop()
    print("stopped")
    root.destroy()

def controller():
    pauseBtn=tk.Button(text="Pause",command=pause, width=10,height=3)
    pauseBtn.pack(side="left")
    playBtn=tk.Button(text="Play",command=resumed, width=10,height=3)
    playBtn.pack(side="right")
    playBtn=tk.Button(text="Stop",command=stopped, width=10,height=3)
    playBtn.pack(side="bottom")
    root.mainloop()



addInPlaylist(n)



