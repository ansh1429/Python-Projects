from tkinter import *
import json
import requests

root = Tk()


root.geometry("500x500")

url = "https://api.exchangerate-api.com/v4/latest/INR"
data = requests.get(url)
# print(data)
res = data.text
main = json.loads(res)
# print(main)

lbl = Label(root, text="enter amount : ")
lbl.pack()
inp = Entry(root)
inp.pack()
lbl2 = Label(root, text="enter country code :")
lbl2.pack()
inp2 = Entry(root)
inp2.pack()

txt = Text(root, width=50, bg="skyblue", fg="black")
txt.pack()


def convert():
    a = int(inp.get())
    b = inp2.get().upper()
    for i in main["rates"]:
        if i == b:
            ans = main["rates"][i] * a
            txt.insert("0.0", "currency in " + i + " " + str(ans))


btn = Button(root, text="convert", command=convert)
btn.pack()

root.mainloop()
