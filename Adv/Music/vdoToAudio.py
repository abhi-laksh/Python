import moviepy.editor as mp



clip=mp.VideoFileClip("sam.mp4")
clip.subclip(0,200)
clip.audio.write_audiofile("audio.mp3")