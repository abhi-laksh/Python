import os
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


def  getSize(size):
    #2**10 = 1024
    power = 2**10
    n = 0
    Dic_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /=  power
        n += 1
    return str(int(size)) 

def progress_function(self,chunk,file_handle, bytes_remaining):

	size = strms.filesize
	p = 0
	while p <= 100:
		progress = p
		print(str(p)+'%')
		p = percent(self,bytes_remaining, size)

def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

global strms

def progress_function(stream, chunk, file_handle, bytes_remaining):
	global strms
	print(round((1-bytes_remaining/strms.filesize)*100, 3), '% done...' ,end="\r")

urll='https://www.youtube.com/playlist?list=PLWPirh4EWFpG49yASGCmvOwXwVvgnm6Jt'
base = "http://www.youtube.com"
pl=Playlist(urll)
s = pl.parse_links()
# strm = yt.streams.all()
# yt.download_all(res="720p")
full = []
print("Setting links....")
for subLink in s:
	eachLink = base + subLink
	full.append(eachLink)
# for each in full:

# 	yt = YouTube(each, on_progress_callback=progress_function)
# 	strms = yt.streams.filter(res='360p',file_extension='mp4').first()
# 	# ,file_extension='mp4'
# 	# print("Size is : " + getSize(strms.filesize))
# 	total += int(getSize(strms.filesize))
# 	# print("Download in progress : " , )
# 	# print(strms)
# 	# strms.download("./")
# 	print("Size : " , total , end="\r")
# 	# break

print(len(full))
# arrToDownload = ['4', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '19', '20','21', '22', '24', '25', '26', '28', '29', '30', '31', '32', '33', '34', '36', '37', '38']
# # arrToDownload = ['4', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '19', '20','21', '22', '24', '25', '26', '28', '29', '30', '31', '32', '33', '34', '36', '37', '38', '47', '48', '49', '50', '51', '57', '58', '59', '60', '61', '71', '72', '73', '74', '75', '76', '77', '82', '83']
# vidoes = []
# for nums in arrToDownload:
# 	link = full[int(nums)-1]
# 	vidoes.append(link)

# print(len(vidoes))
# print(arrToDownload[:4])
# print(arrToDownload[21:29])

# def downloadVid(vidList):
# 	global strms
# 	for each in vidList:
# 		yt = YouTube(each,on_progress_callback=progress_function)
# 		strms = yt.streams.filter(res='360p',file_extension='mp4').first()
# 		# ,file_extension='mp4'
# 		print("Size is : " + getSize(strms.filesize))
# 		print("Downloading : " , strms.default_filename[:30])
# 		strms.download("./Comm_Systems/")

# downloadVid(full[12:16])
