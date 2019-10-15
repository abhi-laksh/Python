import os
from os import listdir
from os.path import isfile , join

try:
	from pytube import Playlist
	from pytube import YouTube
	from multiprocessing import Process
	from threading import Thread
except:
	os.system("pip install multiprocessing")
	from pytube import Playlist
	from pytube import YouTube
	from multiprocessing import Process


# def  getSize(size):
#     #2**10 = 1024
#     power = 2**10
#     n = 0
#     Dic_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
#     while size > power:
#         size /=  power
#         n += 1
#     return str(int(size)) 

# # def progress_function(self,chunk,file_handle, bytes_remaining):

# # 	size = strms.filesize
# # 	p = 0
# # 	while p <= 100:
# # 		progress = p
# # 		print(str(p)+'%')
# # 		p = percent(self,bytes_remaining, size)

# # def percent(self, tem, total):
# #     perc = (float(tem) / float(total)) * float(100)
# #     return perc

# global strms

# def progress_function(stream, chunk, file_handle, bytes_remaining):
# 	global strms
# 	print(round((1-bytes_remaining/strms.filesize)*100, 3), '% done...' ,end="\r")

urll = 'https://www.youtube.com/playlist?list=PLgwJf8NK-2e7uyUYrpgUUQowmRuKxRdwp' 
base = "http://www.youtube.com"
pl=Playlist(urll)
s = pl.parse_links()
p = "C:\\Users\\Abhishek\\Desktop\\DS"
videoName = os.listdir(p)
full = []
notFound = []
print("Setting links....")
for subLink in s:
	eachLink = base + subLink
	full.append(eachLink)
infoss = []
def downloadVid(vidList):
	global strms
	for each in vidList:
		number = vidList.index(each)
		yt = YouTube(each)
		strms = yt.streams.filter(res='144p',file_extension='mp4').first()
		namevid = strms.default_filename
		data = (number , namevid)
		infoss.append(data)
		print("inserted : " , namevid)
		try:
			pos = videoName.index(namevid)
			oldName = join(p , videoName[pos])
			newName = join(p , str(number)+ ". " + videoName[pos])
			# newName = str(number)+ ". " + videoName[pos]
			os.rename(oldName,newName)
		except ValueError:
			infos = (str(number), namevid , each)
			notFound.append(infos)

downloadVid(full)
# print(videoName)
# print(notFound)
print(infos)
	


# print(len(full))
# os.rename()
# print(a)
# downloadVid(nott)