import moviepy.editor as mp


name=input("name : ")
named=input("name of trimmed file: ")
clip=mp.AudioFileClip(name + ".mp3")
sbClip=clip.subclip(60,70)
sbClip.write_audiofile(named + ".wav")