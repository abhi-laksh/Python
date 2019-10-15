#--- DATE : June 17, 2019 | 18:04:45
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Get movie names from folders (Keep it near main folder e.g - MOVIES)
about='Get movie names from folders'
print('About :' + about)
import os
try:
	import shutil
except ModuleNotFoundError:
	os.system("python -m pip install shutil")

curDir = os.getcwd()
def findAllMovies(mainDir,found=True):
	dirs = os.walk(mainDir)
	