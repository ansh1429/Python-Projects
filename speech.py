from tkinter import *
import pyttsx3
root=Tk()
root.geometry("300x300")


lbl=Label(root,text="enter a sentence : ")
lbl.pack()
inp=Entry(root)
inp.pack()

def say():
    a=inp.get()
    speech = pyttsx3.init()
    speech.setProperty('rate', 50)  
    speech.say(a)
    speech.runAndWait()
    


btn=Button(root,text="speak",command=say)
btn.pack()

root.mainloop()