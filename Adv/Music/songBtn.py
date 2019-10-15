import tkinter as tk
import pygame

# Function to play a song
roo=tk.Tk()

def musicPlayer(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        print("Playing song")
        pygame.time.Clock().tick(10)
        controler()




files=input("Enter the file path : ")

def pause():
    pygame.mixer.music.pause()
    print("paused")

def resumed():
    pygame.mixer.music.unpause()
    print("playing")

def stopped():
    pygame.mixer.music.stop()
    print("stopped")
    roo.destroy()

def controler():
    pauseBtn=tk.Button(text="Pause",command=pause, width=10,height=3)
    pauseBtn.pack(side="top")
    playBtn=tk.Button(text="Play",command=resumed, width=10,height=3)
    playBtn.pack(side="top")
    playBtn=tk.Button(text="Stop",command=stopped, width=10,height=3)
    playBtn.pack(side="top")
    roo.mainloop()
    

if files!='':
    musicPlayer(files)
else:
    print("Error")


# texts="Hi"
# def display():
#     print(texts)
    # btn.config(texts)


# btn=tk.Button(text="Ok",command=display, width=10,height=3)
# btn.grid(row=1,column=1)