# Dominic Lye 2022
# Added to Github in 2024
# Lots of bad coding practices, interesting to see my old code.

import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkcalendar import DateEntry
from tkinter import filedialog as fd
import csv
from os.path import exists

# Add the order to an existing csv file, if it doesn't exist, a new one will be created.
def add_to_order():
    calculate_cost()
    dictOrder = {
        'Name': f'{entName.get()}',
        'Email': f'{entEmail.get()}',
        'Date': f'{selDate.get_date()}',
        'Paid': f'{cmbPaymentConfirmed.get()}',
        'Shirt_Type': f'{strType.get()}',
        'Shirt_Style': f'{strStyle.get()}',
        'Shirt_Size': f'{strSize.get()}',
        'Colour': f'{lblColourDisplay["text"]}',
        'Logo_Front': f'{filenameFront}',
        'Logo_Back': f'{filenameBack}',
        'Quantity': f'{spnQuantity.get()}',
        'Cost': f'{lblCostNumber["text"]}'
    }
    header = ['Name', 'Email', 'Date', 'Paid', 'Shirt_Type', 'Shirt_Style', 'Shirt_Size', 'Colour', 'Logo_Front', 'Logo_Back', 'Quantity', 'Cost']
    if exists('order_profiles.csv'):
        with open('order_profiles.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writerow(dictOrder)
    else:
        with open('order_profiles.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerow(dictOrder)

# Clear the user's Inputs
def clear_inputs():
    entName.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    cmbPaymentConfirmed.delete(0, tk.END)
    lblFrontLogo['text'] = "None"
    lblBackLogo['text'] = "None"
    lblColourDisplay['bg'] = "white"
    lblColourDisplay['text'] = ""
    spnQuantity.delete(0, tk.END)
    for x in range(len(sizes)):
        sizebutton = frmShirtSize.nametowidget(f"sizebutton{x}")
        sizebutton.state(["!selected"])
    for x in range(len(styles)):
        stylebutton = frmShirtStyle.nametowidget(f"stylebutton{x}")
        stylebutton.state(["!selected"])
    for x in range(len(types)):
        typebutton = frmShirtType.nametowidget(f"typebutton{x}")
        typebutton.state(["!selected"])
    lblCostNumber['text'] = '$0'

# Set the filename for the CSV file and the logo label
filenameFront = None
def nameFrontLogo():
    global filenameFront
    filenameFront = fd.askopenfilename()
    print(filenameFront)
    dispFileNameFront = filenameFront.split('/')[len(filenameFront.split('/'))-1]
    lblFrontLogo['text'] = dispFileNameFront

# Set the filename for the CSV file and the logo label
filenameBack = None
def nameBackLogo():
    global filenameBack
    filenameBack = fd.askopenfilename()
    print(filenameBack)
    dispFileNameBack = filenameBack.split('/')[len(filenameBack.split('/'))-1]
    lblBackLogo['text'] = dispFileNameBack

#Calculate the cost of an order profile
def calculate_cost():
    styles = {
        'V-Neck': 2,
        'Polo': 5,
        'Long Sleeve': 5,
        'Normal': 0
    }
    shirt_type = strType.get()
    shirt_size = strSize.get()
    shirt_style = strStyle.get()
    quantity = spnQuantity.get()
    base_cost = 12
    total_cost = 0
    if int(quantity) > 5:
        base_cost = 11
    elif int(quantity) > 10:
        base_cost = 10
    total_cost += styles[shirt_style]
    if shirt_size == "XXL":
        total_cost += 2
    if shirt_type == 'Children':
        total_cost +- 2
    if lblFrontLogo['text'] != "None":
        total_cost += 5
    if lblBackLogo['text'] != "None":
        total_cost += 10
    total_cost += base_cost
    total_cost *= int(quantity)
    print(total_cost)
    lblCostNumber['text'] = f'${total_cost}'

root = tk.Tk()
root.title('Order Processing v1')
root.geometry('700x500')
root.resizable(False, False)

types = ["Men", "Women", "Children"]
sizes = ["XS", "S", "M", "L", "XL", "XXL"]
styles = ["Normal", "V-Neck", "Polo", "Long Sleeve"]

strType = tk.StringVar()
strStyle = tk.StringVar()
strSize = tk.StringVar()
intQuantity = tk.IntVar()

# Create the frame on the left side of the software, used for storing customer info
frmCustomerInformation = tk.LabelFrame(root, text='Customer Information', borderwidth=3, relief='groove', width=200)
frmCustomerInformation.grid(row=0, column=0, padx=10, ipadx=10, sticky="n")

# Create the frame on the right side of the software, used to customize the shirt
frmShirtCustomization = tk.LabelFrame(root, text="Shirt Customization", borderwidth=3, relief='groove')
frmShirtCustomization.grid(row=0, column=2, sticky="e", padx=10, rowspan=5)

# Full Name Entry and Label
lblName = ttk.Label(frmCustomerInformation, text='Name:')
lblName.grid(row=0, column=0, columnspan=2, sticky="w")
entName = ttk.Entry(frmCustomerInformation, width=10)
entName.grid(row=0, column=1, sticky="w")

# Email Entry and Label
lblEmail = ttk.Label(frmCustomerInformation, text='Email:')
lblEmail.grid(row=1, column=0)
entEmail = ttk.Entry(frmCustomerInformation)
entEmail.grid(row=1, column=1)

# Order Date Label and Selection
lblDate = ttk.Label(frmCustomerInformation, text="Date:")
lblDate.grid(row=2, column=0)
selDate = DateEntry(frmCustomerInformation)
selDate.grid(row=2, column=1, sticky="w")

# Payment Confirmed Label and Spinbox
lblPaymentConnfirmed = ttk.Label(frmCustomerInformation, text="Paid:")
lblPaymentConnfirmed.grid(row=3, column=0)
cmbPaymentConfirmed = ttk.Combobox(frmCustomerInformation, values=["Yes", "No"], width=5)
cmbPaymentConfirmed.grid(row=3, column=1, sticky="w")

#Shirt Type
frmShirtType = ttk.LabelFrame(frmShirtCustomization, text="Shirt Type", borderwidth=3, relief='ridge')
frmShirtType.grid(row=0, column=0, padx=10, pady=20, sticky="w")

for x, type in enumerate(types):
    btnShirtType = ttk.Radiobutton(frmShirtType, text=f"{str(type)}", variable=strType, value=type, name=f"typebutton{x}")
    btnShirtType.grid(row=0, column=x, padx=10)


#Shirt Style
frmShirtStyle = ttk.LabelFrame(frmShirtCustomization, text="Shirt Style", borderwidth=3, relief="ridge")
frmShirtStyle.grid(row=1, column=0, padx=10)

for x, style in enumerate(styles):
    btnShirtStyle = ttk.Radiobutton(frmShirtStyle, text=f"{str(style)}", variable=strStyle, value=style, name=f"stylebutton{x}")
    btnShirtStyle.grid(row=0, column=x, padx=10)

#Shirt Size
frmShirtSize = ttk.LabelFrame(frmShirtCustomization, text="Shirt Size", borderwidth=3, relief="ridge")
frmShirtSize.grid(row=2, column=0, padx=10, sticky="w", pady=20)

for x, size in enumerate(sizes):
    btnShirtSize = ttk.Radiobutton(frmShirtSize, text=f"{str(size)}", variable=strSize, value=size, name=f"sizebutton{x}")
    btnShirtSize.grid(row=0, column=x, padx=10)

#Colour Picker
frmColourPicker = ttk.LabelFrame(frmShirtCustomization, text="Shirt Colour", borderwidth=3, relief="ridge", width=40)
frmColourPicker.grid(row=3, column=0, padx=10, sticky="w")

def shirt_colour():
    colour = askcolor()[1]
    lblColourDisplay['text'] = colour
    lblColourDisplay['bg'] = colour

btnColourPicker = ttk.Button(frmColourPicker, text="Shirt Colour", command=shirt_colour)
btnColourPicker.grid(row=0, column=0, sticky="w")

lblColourDisplay = tk.Label(frmColourPicker,text="#ffffff", bg="#ffffff", width="20", fg='black')
lblColourDisplay.grid(row=0, column=1, sticky="w")

#Logos
frmLogos = ttk.LabelFrame(frmShirtCustomization, text="Logo Customization", borderwidth=3, relief="groove")
frmLogos.grid(row=4, column=0, pady=20, sticky="w", padx=10)


btnFrontLogo = ttk.Button(frmLogos, text="Front Logo", command=nameFrontLogo).grid(row=0, column=0)
btnBackLogo = ttk.Button(frmLogos, text="Back Logo", command=nameBackLogo).grid(row=1, column=0)

lblFrontLogo = ttk.Label(frmLogos, text="None")
lblFrontLogo.grid(row=0, column=1)

lblBackLogo = ttk.Label(frmLogos, text="None")
lblBackLogo.grid(row=1, column=1)

#Quantity
frmQuantity = ttk.LabelFrame(frmShirtCustomization, text="Quantity", borderwidth=3, relief="groove")
frmQuantity.grid(row=5, column=0, padx=10, sticky="w")

spnQuantity = ttk.Spinbox(frmQuantity, from_=1, to=50)
spnQuantity.grid(row=0, column=0)

#Cost
frmCost = tk.LabelFrame(root, text="Cost", borderwidth=3, relief="groove")
frmCost.grid(row=1, column=0, sticky="n", padx=10, ipadx=10, columnspan=2)

btnCalcCost = ttk.Button(frmCost, text="Calculcate Cost", command=calculate_cost)
btnCalcCost.grid(row=0, column=0, sticky="w", columnspan=2)

lblCost = ttk.Label(frmCost, text="Cost: ")
lblCost.grid(row=1, column=0, sticky="w")

lblCostNumber = ttk.Label(frmCost, text="$0")
lblCostNumber.grid(row=1, column=1, sticky="w")

#File Button and Clear Button

btnAddToFile = ttk.Button(root, text="Add to File", width="8", command=add_to_order)
btnAddToFile.grid(row=2, column=0, sticky="n")

btnClearInput = ttk.Button(root, text="Clear Inputs", command=clear_inputs)
btnClearInput.grid(row=3, column=0, sticky="n")

root.mainloop()