import tkinter as tk
root = tk.Tk()
data:str
def take():
    inp= tk.Entry(root , textvariable=data)
    inp.insert(0,"Want to trim ? {y/n) : ")
    inp.pack()
    inp.focus_set()
    return inp
take()
def write():
    
    print(take().get()[0])
    root.destroy()





# e = tk.Entry(root)
# e.insert(10,"Enter Something")

# e.pack()
# e.focus_set()

b = tk.Button(root,text='okay',command=write)
b.pack(side='bottom')


root.mainloop()