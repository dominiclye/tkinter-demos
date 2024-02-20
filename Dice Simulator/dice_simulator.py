# This task will create a dice roller
# application that allows the user to
# choose the size of the dice and then get
# a random roll calculated and displayed


import tkinter as tk
from tkinter import Variable, ttk
from random import randint

root = tk.Tk()
root.title("Dice Simulator Version 2")
root.geometry("300x300")

# variables to store the size of the dice,
# the number of dice, the random result of a rolls
# and the total
intSides = tk.IntVar(value=0)
intDice = tk.IntVar(value=1)
intTotal = tk.IntVar(value=0)
strRolls = tk.StringVar()


def roll_die():
    """
    Uses the intDie variable to set the size
    of the die to roll and sets the result
    variable using randint to generate a
    random roll.
    """

    # Check that a die size has been selected
    # otherwise do nothing.
    if intSides.get() > 0:
        # Create a list to store the rolls
        diceRolls = []
        strRolls.set("")
        for roll in range(intDice.get()):
            diceRolls.append(randint(1, intSides.get()))
        # Update the rolls
        strRolls.set("+".join(map(str, diceRolls)))
        lblResults["text"] = strRolls.get()
        # Update the totals
        intTotal.set(sum(diceRolls))
        lblTotal["text"] = intTotal.get()


# make the grid columns to the same width
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# use a dictionary to store the different die sizes
die = {
    "Four": 4,
    "Six": 6,
    "Eight": 8,
    "Ten": 10,
    "Twelve": 12,
    "Twenty": 20,
    "One Hundred": 100,
}

# Add a heading widget. Use the anchor property
# to get the label text centered
lblHeading = ttk.Label(
    root,
    text="Roll your Dice",
    font="default 20",
    anchor="center",
)

# Add widgets for the die sizes to a label frame
lbfSides = ttk.LabelFrame(root, text="Number of Sides")

# Use a loop to go through the die dictionary. Use the key
# and value for each dictionary item to create a radio
# button as a die size. Link each button to the same
# variable so they are in a group and then pack them
# into the frame.
for key, value in die.items():
    lbl = ttk.Radiobutton(lbfSides, text=key, value=value, variable=intSides)
    lbl.pack(side="top", fill="x")

# Create a frame to hold the spinbox and labels to roll
# the dice and show the results. Then pack the widgets
frmResults = ttk.Frame(root)
lblNumberHeading = ttk.Label(frmResults, text="Number of Dice")
spnNumberOfDice = ttk.Spinbox(frmResults, from_=1, to=6, textvariable=intDice, width=5)
lblResultHeading = ttk.Label(frmResults, text="Results", font="default 12")
lblResults = ttk.Label(frmResults, text=strRolls.get(), font="default 10")
lblTotalHeading = ttk.Label(frmResults, text="Total", font="default 16")
lblTotal = ttk.Label(
    frmResults, text=str(intTotal.get()), font="default 30", relief="groove", padding=10
)

# Use a loop to pack the widgets in the results frame
for widget in frmResults.winfo_children():
    widget.pack()

# Create the button to roll the dice
btnRoll = ttk.Button(root, text="Roll", command=roll_die)

# Use a grid layout on the main window to show the heading
# and frames. Use the grid to layout the items nicely.
lblHeading.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="ew")
lbfSides.grid(column=0, row=1)
frmResults.grid(column=1, row=1)
btnRoll.grid(column=0, row=2, columnspan=2, pady=30)

root.mainloop()
