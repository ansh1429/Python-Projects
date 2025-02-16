from tkinter import *

root = Tk()
root.geometry("500x500")

lbl = Label(root, text="enter year : ")
lbl.pack()
inp = Entry(root)
inp.pack()


def fun1():
    txt.delete("0.0", END)
    a = int(inp.get())

    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        txt.insert("0.0", str(a) + " is a leap year")
    else:
        txt.insert("0.0", str(a) + " is not a leap year")


txt = Text(root, width=50, bg="skyblue", fg="white")
txt.pack()

btn = Button(root, text="submit", command=fun1)
btn.pack()

root.mainloop()
