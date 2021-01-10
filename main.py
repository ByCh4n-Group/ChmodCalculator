import tkinter as tk
import os
from modules import *

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

banner = Beyaz+"""
██╗      ██████╗  ██████╗ ███████╗
██║     ██╔═══██╗██╔════╝ ██╔════╝
██║     ██║   ██║██║  ███╗███████╗
██║     ██║   ██║██║   ██║╚════██║
███████╗╚██████╔╝╚██████╔╝███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
"""

print(banner)

window = tk.Tk()
#Head
window.title("Chmod Calculator")
window.geometry("500x250")
window.resizable(False,False)
window.iconbitmap(r"simge.ico")

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


#function
value=0
def chx():
    value=0
    if owner1.get() == 0:
        pass
    else:
        value+=400
    if owner2.get() == 0:
        pass
    else:
        value+=200
    if owner3.get() == 0:
        pass
    else:
        value+=100

    if group1.get() == 0:
        pass
    else:
        value+=40
    if group2.get() == 0:
        pass
    else:
        value+=20
    if group3.get() == 0:
        value+0
    else:
        value+=10
    
    if other1.get() == 0:
        pass
    else:
        value+=4
    if other2.get() == 0:
        pass
    else:
        value+=2
    if other3.get() == 0:
        pass
    else:
        value+=1
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print(value)

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

result = tk.Label(window, text="Our answer will appear in Terminal", font="20")
result.pack()
result.place(x=125, y=175)

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


window.mainloop()
