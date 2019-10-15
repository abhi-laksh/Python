import os

dele=''

def takingNames():
    howMuch= int(input('Enter number folders you want to create : '))
    paths=input('Enter path :  ')
    dirName = []
    paths.replace('\\',"\\\\")
    print(paths)
    for i in range(1, howMuch+1):
        askName=input('Enter name for directory')
        folderName= paths +  "\\\\" + askName
        
        print(folderName)
        dirName.append(folderName)
    createFolder(dirName)

def createFolder(name):
    for folder in name:
        print(folder)
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Directory => ", folder, " created")
        else:
            print("Directory => ", folder, " already exists")

takingNames()