import pygame

files=input("Enter the file path : ")
if files!='':
    pygame.mixer.init()
    pygame.mixer.music.load(files)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
        askToPause=str(input("Enter P for pause:"))[0]
        if askToPause=='p':
            pygame.mixer.music.pause()
            askToPlay=str(input("Enter pl for play :"))
            if askToPlay=='pl':
                pygame.mixer.music.unpause()
else:
    print("Error")

