import pygame
musicArr=['1.mp3','2.mp3','3.mp3']

for song in musicArr:
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

