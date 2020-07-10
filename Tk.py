"""
import tkinter

window = tkinter.Tk()
window.title("Hey Its Me, Welcome!!")
window.geometry("300x300")




window.mainloop()
"""

# WIDGETS  CHECK BUTTON
"""
from tkinter import *
softwarica = Tk()
var1 = IntVar()
Checkbutton(softwarica, text='Computing A', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(softwarica, text='Computing B', variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(softwarica, text='Ethical', variable=var3).grid(row=2, sticky=W)
var4 = IntVar()
mainloop()
"""

# WIDGETS ENTRY
"""
from tkinter import *
softwarica = Tk()
softwarica.title("Welcome to Our College")
Label(softwarica, text="Student's First Name").grid(row=0)
Label(softwarica, text="Student's Last Name").grid(row=1)
e1 = Entry(softwarica)
e2 = Entry(softwarica)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
"""
# SElF LEARNING

"""
from tkinter import *
shas = Tk()
shas.title("Random tkinter PRACTICE")
Label(shas, text="How you?",font=("Aeiral", 15)).grid(row=0)
Label(shas, text="Do you want sth?",font=("Aeiral", 15)).grid(row=1)
shas.geometry("500x500")
en1 = Entry(shas)
en2 =Entry(shas)
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)

mainloop()
"""
"""
from tkinter import *

shas = Tk()
shas.title("HEllO TKINTER")
shas.geometry("250x500")
v1 = IntVar()
Checkbutton(shas, text="Are you an adult?", font=("Aeiral", 15)).grid(row=0)
Checkbutton(shas, text="Do you want sth?", font=("Aeiral", 15)).grid(row=1)
Label(shas, text="How are you?", font=("Aeiral", 15)).grid(row=3)
en1 =Entry(shas)
en1.grid(row=3, column=5)
mainloop()
"""
# PERSONAL DETAILS

"""
from tkinter import *

shas = Tk()
shas.title("Fill up the form")
shas.geometry("500x500")
Label(shas, text="Enter your FULL name: ", font=("Aerial", 15)).grid(row=1)
en1 = Entry(shas)
en1.grid(row=1, column=1)
Label(shas, text="Address: ", font=("Aerial", 15)).grid(row=2)
en2 = Entry(shas)
en2.grid(row=2, column=1)
Label(shas, text="E-mail Address: ", font=("Aerial", 15)).grid(row=3)
en3 = Entry(shas)
en3.grid(row=3, column=1)
Label(shas, text="Pick your gender please:", font=("Aerial", 15)).grid(row=4)
Checkbutton(shas, text="Male", font=("Aerial", 15)).grid(row=5)
Checkbutton(shas, text="Female", font=("Aerial", 15)).grid(row=6)



mainloop()
"""
