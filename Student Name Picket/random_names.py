# This is a simple tkinter app
# Dominic Lye 2022

import tkinter as tk
from tkinter import ttk
from random import choice

# Set the title, screen size and resizable values
# for our simple window. We want something like
# a basic phone screen size size.
root = tk.Tk()
root.title("Pick a name at random")
root.geometry("400x500")
root.resizable(False, False)

# Variables to hold the list of names to pick from
students = []
strNames = tk.StringVar(value=students)

strNewName = tk.StringVar()

def get_name():
    """
    Pick a name at random from the available list of names
    """

    # print(strNames.get())
    # print(type(strNames.get()))
    pick = choice(eval(strNames.get()))
    lblRandomName.config(text=pick)


def clear():
    """
    Clear the random name
    """

    lblRandomName["text"] = ""
    lstNames.delete(0, tk.END)


def add_name():
    """
    Get the new name, add it to the list and
    clear the widget ready for another new name.
    """
    
    students.append(strNewName.get())
    strNames.set(students)
    lstNames.config(listvariable=strNames)
    entAddName.delete(0, tk.END)

# A frame and widgets to display the list of names to choose
# from when picking a random name.
frmNames = tk.Frame(root)
lblNames = ttk.Label(frmNames, text="List of Student Names")
lstNames = tk.Listbox(frmNames, height=5, listvariable=strNames)

frmNames.grid(row=0, column=0)
lblNames.pack()
lstNames.pack()

# Frame to add names to the list box
frmAddNames = tk.Frame(root)
lblAddNameHeading = ttk.Label(frmAddNames, text='Add a name to the list')
entAddName = ttk.Entry(frmAddNames, textvariable=strNewName)
btnAddName = ttk.Button(frmAddNames, text="Add a new name", command=add_name)

frmAddNames.grid(row=0, column=1)
lblAddNameHeading.pack()
entAddName.pack()
btnAddName.pack()

# A frame and labels to hold the random name selected
# and display it under the list of names
frmRandom = tk.Frame(root)
lblRandomHeader = ttk.Label(frmRandom, text="Our pick is:")
lblRandomName = ttk.Label(frmRandom)

frmRandom.grid(row=1, column=0)
lblRandomHeader.pack()
lblRandomName.pack()

# Buttons are added now to the bottom of the form
frmButtons = tk.Frame(root)
btnClear = ttk.Button(frmButtons, text="Clear", command=clear)
btnGetName = ttk.Button(frmButtons, text="Pick a name", command=get_name)

frmButtons.grid(row=2, column=0)
btnClear.pack(side="left")
btnGetName.pack(side="right")

root.mainloop()
