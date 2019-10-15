import os
import shutil


mainDir = os.getcwd()
# toCopy = "create_py_file.py"
toCopy = [os.path.basename(__file__) , "create_py_file.py" , "runPython.py" ]
dirs = os.walk(mainDir)
allDirsPath = []
for root , d , files in list(dirs):
	for name in d:
		if not "." in name and not "_" in name:
			flders = os.path.join(root , name)
			allDirsPath.append(flders)

# dirs = [d for d in os.listdir(mainDir) if os.path.isdir(os.path.join(mainDir , d)) and d !=".idea"]
# print(allDirsPath)

for each in allDirsPath:
	if isinstance(toCopy,list):
		for i in toCopy:
			shutil.copy(i,each)
			# os.remove(os.path.join(each,i))
	else:
		shutil.copy(toCopy,each)
		# os.remove(os.path.join(each,toCopy))