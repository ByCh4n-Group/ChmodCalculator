import tkinter as tk
import os, time, pyperclip
from tkinter import messagebox
from modules import *
from tkinter.filedialog import askopenfilename

if os.name == "nt":
    if os.path.isfile(".\modules.py") == True:
        pass
elif os.name == "posix":
    if os.path.isfile("./modules.py") == True:
        pass     


window = tk.Tk()
#Head
window.title("Chmod Calculator")
window.geometry("500x350")
window.resizable(False,False)


#Body


#Owners
owner1 = tk.IntVar()
owner2 = tk.IntVar()
owner3 = tk.IntVar()

owner1.set(0)
owner2.set(0)
owner3.set(0)

#Groups

group1 = tk.IntVar()
group2 = tk.IntVar()
group3 = tk.IntVar()

group1.set(0)
group2.set(0)
group3.set(0)

#Others

other1 = tk.IntVar()
other2 = tk.IntVar()
other3 = tk.IntVar()

other1.set(0)
other2.set(0)
other3.set(0)


#functions
value=""
def chx():
    global value
    value=0 
    if owner1.get() == 0:
        rwx1.config(text="-")
    else:
        value+=400
        rwx1.config(text="r")
        if value >=100 or value <= 700:
            zero.config(text="")
            zero.place(x=100 , y=175)
    if owner2.get() == 0:
        rwx2.config(text="-")
    else:
        value+=200
        rwx2.config(text="w")
        if value >=100 or value <= 700:
            zero.config(text="")
            zero.place(x=100 , y=175)
    if owner3.get() == 0:
        rwx3.config(text="-")
    else:
        value+=100
        rwx3.config(text="x")
        if value >=100 or value <= 700:
            zero.config(text="")
            zero.place(x=100 , y=175)


    if group1.get() == 0:
        rwx4.config(text="-")
    else:
        value+=40
        rwx4.config(text="r")
        if value >= 10 and value <= 70:
            zero.config(text="0")
            zero.place(x=158 , y=175)
    if group2.get() == 0:
        rwx5.config(text="-")
    else:
        value+=20
        rwx5.config(text="w")
        if value >= 10 and value <= 70:
            zero.config(text="0")
            zero.place(x=158 , y=175)
    if group3.get() == 0:
        rwx6.config(text="-")
    else:
        value+=10
        rwx6.config(text="x")
        if value >= 10 and value <= 70:
            zero.config(text="0")
            zero.place(x=158 , y=175)
    

    if other1.get() == 0:
        rwx7.config(text="-")
    else:
        value+=4
        rwx7.config(text="r")
        if value >= 1 and value <= 7:
            zero.config(text="00")
            zero.place(x=150 , y=175)
    if other2.get() == 0:
        rwx8.config(text="-")
    else:
        value+=2
        rwx8.config(text="w")
        if value >= 1 and value <= 7:
            zero.config(text="00")
            zero.place(x=150 , y=175)
    if other3.get() == 0:
        rwx9.config(text="-")
    else:
        value+=1
        rwx9.config(text="x")
        if value >= 1 and value <= 7:
            zero.config(text="00")
            zero.place(x=150 , y=175)
    if value == 0:
        result.config(text="000")

    result.config(text=value)
path=""
def askfile():
    filepath = askopenfilename()
    global path
    path = "chmod "+str(value)+" "+ filepath
def copy():
    pyperclip.copy(path)

#Owner

label = tk.Label(window, text="Owner", font="20")
label.pack(side=tk.LEFT)
label.place(x=50,y=0)

checkbox4 = tk.Checkbutton(window, text="Read", font="15", variable=owner1, command=chx)
checkbox4.pack()
checkbox4.place(x=50, y=35)

checkbox5 = tk.Checkbutton(window, text="Write", font="15", variable=owner2, command=chx)
checkbox5.pack()
checkbox5.place(x=50, y=75)

checkbox6 = tk.Checkbutton(window, text="Execute", font="15", variable=owner3, command=chx)
checkbox6.pack()
checkbox6.place(x=50, y=105)

#Group
label2 = tk.Label(window, text="Group", font="20")
label2.pack()

result = tk.Label(window, text=" ", font="20")
result.pack()
result.place(x=170, y=175)

zero = tk.Label(window, text=" ", font="20")
zero.pack()
zero.place(x=130 , y=175)


rwx1 = tk.Label(window, text="-", font="20")
rwx1.pack()
rwx1.place(x=300, y=175)

rwx2 = tk.Label(window, text="-", font="20")
rwx2.pack()
rwx2.place(x=315, y=175)

rwx3 = tk.Label(window, text="-", font="20")
rwx3.pack()
rwx3.place(x=330, y=175)

bosluk1 = tk.Label(window, text=" ")
bosluk1.pack()
bosluk1.place(x=345 ,y=175)


rwx4 = tk.Label(window, text="-", font="20")
rwx4.pack()
rwx4.place(x=360, y=175)

rwx5 = tk.Label(window, text="-", font="20")
rwx5.pack()
rwx5.place(x=375, y=175)

rwx6 = tk.Label(window, text="-", font="20")
rwx6.pack()
rwx6.place(x=390, y=175)

bosluk3 = tk.Label(window, text=" ")
bosluk3.pack()
bosluk3.place(x=405 ,y=175)


rwx7 = tk.Label(window, text="-", font="20")
rwx7.pack()
rwx7.place(x=420, y=175)

rwx8 = tk.Label(window, text="-", font="20")
rwx8.pack()
rwx8.place(x=435, y=175)

rwx9 = tk.Label(window, text="-", font="20")
rwx9.pack()
rwx9.place(x=450, y=175)






checkbox1 = tk.Checkbutton(window, text="Read", font="15", variable=group1, command=chx)
checkbox1.pack()
checkbox1.place(x=210, y=35)

checkbox2 = tk.Checkbutton(window, text="Write", font="15", variable=group2, command=chx)
checkbox2.pack()
checkbox2.place(x=210, y=70)

checkbox3 = tk.Checkbutton(window, text="Execute", font="15", variable=group3, command=chx)
checkbox3.pack()
checkbox3.place(x=210, y=105)

#Other
label3 = tk.Label(window, text="Other", font="20")
label3.pack(side=tk.RIGHT)
label3.place(x=400, y=0)

checkbox7 = tk.Checkbutton(window, text="Read", font="15", variable=other1, command=chx)
checkbox7.pack()
checkbox7.place(x=400, y=35)

checkbox8 = tk.Checkbutton(window, text="Write", font="15", variable=other2, command=chx)
checkbox8.pack()
checkbox8.place(x=400, y=70)

checkbox9 = tk.Checkbutton(window, text="Execute", font="15", variable=other3, command=chx)
checkbox9.pack()
checkbox9.place(x=400, y=105)





askfile = tk.Button(window, text="Select File", command=askfile)
askfile.pack()
askfile.place(x=400,y=250)

copy_button = tk.Button(window, text="Copy Command", command=copy)
copy_button.pack()
copy_button.place(x=400,y=280)

window.mainloop()
