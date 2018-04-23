import os
import sys
import tkinter
import tkMessageBox
def plottingFunc():
    os.system("python plotting.py")
root = tkinter.Tk()
root.title("Motion Detector")
root.geometry("500x400")
label = tkinter.Label(root,text="Click start!")
button = tkinter.Button(root,text="Start",width=15,command= plottingFunc)
label.pack()
button.pack(padx=5,pady=55)
def destroy():
    root.destroy()
closeButton = tkinter.Button(root,text="Close",width=15,command=destroy)
closeButton.pack(pady=5,padx=1)
root.mainloop()