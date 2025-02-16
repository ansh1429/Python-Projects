import phonenumbers
from tkinter import *
from phonenumbers import carrier, geocoder, timezone

root = Tk()

lbl = Label(root, text="enter mobile no : ")
lbl.pack()

inp = Entry(root)
inp.pack()


def fun():
    txt.delete("1.0", END)
    a1 = inp.get()
    no = phonenumbers.parse(a1)
    #print(phonenumbers.parse(91))
    res1 = timezone.time_zones_for_number(no)
    res2 = carrier.name_for_number(no, "en")
    txt.insert("1.0", res1)
    txt.insert("1.0", "The timezone is : ")

    txt.insert("1.0", "\n")
    txt.insert("1.0", res2)
    txt.insert("1.0", "The Sim Network is : ")


btn = Button(root, text="click", command=fun)
btn.pack()

txt = Text(
    root, width=100, bg="skyblue", fg="white", padx=30, pady=40, font=("Arial", 25)
)
txt.pack()


root.mainloop()


"""
  txt.insert("1.0","The location is : "+res1)
  
  txt.insert("1.0","The Sim Network is : "+res2)

mobileno = input("Enter mobile number with country code: ")
mobileno=phonenumbers.parse(mobileno)
#print(mobileno)
print(timezone.time_zones_for_number(mobileno))
print(carrier.name_for_number(mobileno,"en"))
"""
