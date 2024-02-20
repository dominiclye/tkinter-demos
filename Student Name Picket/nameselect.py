# Dominic Lye 2022
# 2024 update: apparently I made 3 different versions of this program, no clue why. This one is less concise than the other two but seems to look the best.

import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()

root.title("Name Selector")
root.geometry("220x400")

#Program Title Label

title = ttk.Label(root, text="Student Selector", font=("Menlo", 20))
title.grid(row=0, column=0, columnspan=2, pady= 10, padx=10)

# List Variable to be displayed in the box
student_list = []

# String variable from the list
studentVar = tk.StringVar(value=student_list)

strError = tk.StringVar()

# Random Student Name
randVar = tk.StringVar()

lblEntry = ttk.Label(root, text="Student Name:", font=("Menlo", 15))
lblEntry.grid(row=1, column=0, padx=10, columnspan=2)

# Entry for the name of the student
entStudentName = ttk.Entry(root, width=13)
entStudentName.grid(row=2, column=0, sticky="n", columnspan=2)

def random_name():
    """
    Randomly select a name from the listbox
    """
    if not student_list:
        randVar.set("Error: Empty List")
        lblResult.config(text=randVar.get())
    else:
        randVar.set(random.choice(student_list))
        lblResult.config(text=randVar.get())

def update_listbox():
    """
    Update the listbox with the added student
    """
    clear_listbox()
    for name in student_list:
        listbox.insert("end", name)


def clear_listbox():
    """
    This is needed or else the names will stack on eachother, clear listbot and clear list have been split
    into two different functions otherwise the names won't be added to the listbox
    """
    listbox.delete(0, "end")

def clear_list():
    """
    Reset the listbox
    """
    listbox.delete(0, "end")
    student_list.clear()

def addstudent():
    """
    The function for adding the student to the list, error handling has been added for the convenience of the teacher.
    """
    name = entStudentName.get()
    entStudentName.delete(0, "end")
    if listbox.size() <= 4:
        student_list.append(name)
        update_listbox()
        strError.set("")
        lblError.config(text=strError.get())
    else:
        strError.set("Error: Your list exceeds 5 names")
        lblError.config(text=strError.get())

# Buttons and Labels Below
listbox = tk.Listbox(root, listvariable=studentVar, height=5)
listbox.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

btnAddStudent = ttk.Button(root, text="Add Student", command=addstudent, width="10")
btnAddStudent.grid(row=3, column=0, padx=10, columnspan=2, sticky="n")

btnRandom = ttk.Button(root, text="Pick Name", command=random_name, width=10)
btnRandom.grid(row=5, column=0, padx=10, columnspan=2)

btnReset = ttk.Button(root, text="Clear Names", width="10", command=clear_list)
btnReset.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

lblResult = ttk.Label(root, textvariable=str(randVar.get()), borderwidth=3, relief="ridge", width=13)
lblResult.grid(row=6, column=0, padx=10, columnspan=2, sticky="n")

lblError = ttk.Label(root, textvariable=str(strError.get()))
lblError.grid(row=8, column=0, sticky="s")

root.mainloop()