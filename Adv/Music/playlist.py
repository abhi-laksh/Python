import pygame



n=int(input("How many songs you want to add : "))
musicArr=[]

def addInPlaylist(a):
    for i in range(1,a+1):
        files=input("Enter the file path / name : ")
        if files!='':
            musicArr.append(files)
        else:
            print("Error")


def playing():
    for song in musicArr:
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)


addInPlaylist(n)
playing()