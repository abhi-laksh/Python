import tkinter as tk

texts="Hi"
def display():
    print(texts)
    # btn.config(texts)

roo=tk.Tk()
btn=tk.Button(text="Ok",command=display, width=10,height=3)
# btn.grid(row=1,column=1)
btn.pack(side="top")
roo.mainloop()