#Importing modules
import tkinter as tk
from tkinter import *
import os

#Defining the functions 
def takingNames():
    howMuch=  dataNum.get()
    paths= dataPath.get()
    dirName = []
    nameList=[]

    paths.replace('\\',"/")
    print(paths)
    for i in range(1, howMuch+1):
        askName=dataName.get()
        if(askName!=''):
        	folderName= paths +  "/" + askName
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


app=Tk()
#Name will be shown in app panel
app.title("Create Folders ! ")


#Btn
subBtn=Button(app,padx=18,pady=4,font=('Open Sans , Arial',10,'normal'),text="Submit",command=takingNames)
okBtn=Button(app,padx=18,pady=4,font=('Open Sans , Arial',10,'normal'),text="Ok",command=takingNames)
#variable where input from textbox wil stored
dataPath=StringVar()
dataName=StringVar()
dataNum=IntVar()

#label for textbox
label1=Label(app,text="Enter the path : ",relief=RAISED,bd=0)
label2=Label(app,text="How many folders ? ",relief=RAISED,bd=0)
#Taking path and number of folder you want to create
paths=Entry(app,font=('Josefin Sans',14,'normal'),textvariable=dataPath,bd=1,insertwidth=3)
numOfFolders=Entry(app,font=('Josefin Sans',14,'normal'),textvariable=dataNum,bd=1,insertwidth=3)
nameBox=Entry(app,font=('Josefin Sans',14,'normal'),textvariable=dataName,bd=1,insertwidth=3)


nameBox.pack()
subBtn.pack(side="bottom")
okBtn.pack(side="bottom")
label1.pack(side="left")
paths.pack(side="bottom")
label2.pack(side="left")
numOfFolders.pack(side="bottom")
app.mainloop()