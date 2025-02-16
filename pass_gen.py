from tkinter import *
import random
import string
root=Tk()
root.geometry("500x500")

lbl=Label(root,text="enter length : ")
lbl.pack()

inp=Entry(root)
inp.pack()

lblup=Label(root,text="uppercase y or n : ")
lblup.pack()
inpup=Entry(root)
inpup.pack()

lbllp=Label(root,text="lowercase y or n : ")
lbllp.pack()
inplp=Entry(root)
inplp.pack()

lblno=Label(root,text="numbers y or n : ")
lblno.pack()
inpno=Entry(root)
inpno.pack()

lblsc=Label(root,text="special character y or n : ")
lblsc.pack()
inpsc=Entry(root)
inpsc.pack()


def fun():
    txt.delete("1.0",END)
    a=int(inp.get())
    up=inpup.get()
    lp=inplp.get()
    no=inpno.get()
    sc=inpsc.get()
    if(up=='y' and lp=='y' and no=='y' and sc=='y'):
        join= ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation ) 
                           for n in range(a)])
    elif(up=='n' and lp=='y' and no=='y' and sc=='y'):
            join= ''.join([random.choice(string.ascii_lowercase + string.digits + string.punctuation ) 
                               for n in range(a)])
    elif(up=='y' and lp=='n' and no=='y' and sc=='y'):
        join= ''.join([random.choice(string.ascii_uppercase + string.digits + string.punctuation ) 
                           for n in range(a)])
    elif(up=='y' and lp=='y' and no=='n' and sc=='y'):
        join= ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation ) 
                           for n in range(a)])
    elif(up=='y' and lp=='y' and no=='y' and sc=='n'):
        join= ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) 
                           for n in range(a)])
    elif(up=='n' and lp=='n' and no=='y' and sc=='y'):
            join= ''.join([random.choice(string.digits + string.punctuation ) 
                               for n in range(a)])
    elif(up=='n' and lp=='y' and no=='n' and sc=='y'):
        join= ''.join([random.choice(string.ascii_lowercase + string.punctuation ) 
                           for n in range(a)])
    elif(up=='n' and lp=='y' and no=='y' and sc=='n'):
        join= ''.join([random.choice(string.ascii_lowercase  + string.digits) 
                           for n in range(a)])
    elif(up=='y' and lp=='n' and no=='n' and sc=='y'):
        join= ''.join([random.choice( string.ascii_uppercase + string.punctuation ) 
                           for n in range(a)])
    elif(up=='y' and lp=='n' and no=='y' and sc=='n'):
        join= ''.join([random.choice(string.ascii_uppercase + string.digits) 
                           for n in range(a)])
    elif(up=='y' and lp=='y' and no=='n' and sc=='n'):
        join= ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase)
                           for n in range(a)])
    elif(up=='n' and lp=='n' and no=='n' and sc=='y'):
        join= ''.join([random.choice( string.punctuation ) 
                           for n in range(a)])
    elif(up=='y' and lp=='n' and no=='n' and sc=='n'):
        join= ''.join([random.choice( string.ascii_uppercase) 
                           for n in range(a)])
    elif(up=='n' and lp=='y' and no=='n' and sc=='n'):
        join= ''.join([random.choice(string.ascii_lowercase ) 
                           for n in range(a)])
    elif(up=='n' and lp=='n' and no=='y' and sc=='n'):
        join= ''.join([random.choice(string.digits ) 
                           for n in range(a)])
    else:
        join="enter valid value";
        
    txt.insert("1.0",join)    

btn=Button(root,text="Click",command=fun)
btn.pack()
txt=Text(root,width=100,bg="skyblue",fg="black",padx=30,pady=40,font=("Arial",25))
txt.pack()
root.mainloop()