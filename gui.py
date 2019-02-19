from tkinter import *
from Customer import *
from Staff import *
from Store import *
from Product import *
from Order import *


root = Tk()
root.geometry("850x500+0+0")
root.resizable(False, False)
root.title("STORE MANAGEMENT")

### methods ###
def put_entry_row(someFrame):
    someinsideFrame=Frame(someFrame)
    someinsideFrame.pack(side=TOP, fill=BOTH)
    someInsideFrameLabel=Label(someFrame, text="  ", pady=10)
    someinsideFrame.pack(side=TOP)

    someLabel = Label(someinsideFrame, text=" ", padx=10)
    someOneEntry = Entry(someinsideFrame)
    someOneEntry.pack(side=LEFT)
    someLabe1 = Label(someinsideFrame, text=" ", padx=10)
    someLabe1.pack(side=LEFT)
    someTwoEntry = Entry(someinsideFrame)
    someTwoEntry.pack(side=LEFT)
    someLabe2 = Label(someinsideFrame, text=" ", padx=10)
    someLabe2.pack(side=LEFT)
    someThreeEntry = Entry(someinsideFrame)
    someThreeEntry.pack(side=LEFT)
    someLabe3 = Label(someinsideFrame, text=" ", padx=10)
    someLabe3.pack(side=LEFT)
    someFourEntry = Entry(someinsideFrame)
    someFourEntry.pack(side=LEFT)
    someLabe4 = Label(someinsideFrame, text=" ", padx=10)
    someLabe4.pack(side=LEFT)
    someFiveEntry = Entry(someinsideFrame)
    someFiveEntry.pack(side=LEFT)


###############



introLabel = Label(root, text="WELCOME TO STORE MANAGEMENT SYSTEM", fg="#31329F", font="Arial 22")
introLabel.pack(side=TOP)

staffNameLabel = Label(root, text="STAFF NAME", fg="#31329F", font="Arial 14")
staffNameLabel.place(x=10, y=60)

staffName = StringVar()
staffNameEntry = Entry(root, textvariable=staffName)
print(staffName)
staffNameEntry.place(x=155, y=65)

customerIdLabel = Label(root, text="CUSTOMER ID", fg="#31329F", font="Arial 14")
customerIdLabel.place(x=10, y=100)

customerId = StringVar()
customerIdEntry = Entry(root, textvariable=customerId)
print(customerId)
customerIdEntry.place(x=155, y=105)

addProductLabel = Label(root, text="ADD", fg="#31329F", font="Arial 16")
addProductLabel.place(x=10, y=140)


def add_entries():
    put_entry_row(centerFrame)


addButton = Button(root, text="+", bg="#9068be", font="Arial 12", fg="white", padx=15, pady=1, command=add_entries)
addButton.place(x=100, y=135)


centerFrame = Frame(root, bg="brown", bd="0", width=828, height=250, padx=1, pady=1)
centerFrame.place(x=15, y=250)



######## INSIDE FRAME #######
######## grid layout #######
nameLayout = Frame(root, bg="green", bd="1", width=828, height=50, padx=20, pady=1)
nameLayout.place(x=10, y=190)

productNameLabel = Label(nameLayout, text="Product Name", fg="#31329F", font="Arial 12")
productNameLabel.place(x=0, y=0)

productCodeLabel = Label(nameLayout, text="Product Code", fg="#31329F", font="Arial 12")
productCodeLabel.place(x=150, y=2)

productPriceLabel = Label(nameLayout, text="Price", fg="#31329F", font="Arial 12")
productPriceLabel.place(x=300, y=2)

productQuantityLabel = Label(nameLayout, text="Quantity", fg="#31329F", font="Arial 12")
productQuantityLabel.place(x=450, y=2)

productQuantityLabel = Label(nameLayout, text="Points", fg="#31329F", font="Arial 12")
productQuantityLabel.place(x=600, y=2)

###
##
# someFrame = Frame(root, bg="#fff")
# someFrame.pack(side=BOTTOM, fill=BOTH)
put_entry_row(centerFrame)
put_entry_row(centerFrame)
put_entry_row(centerFrame)
put_entry_row(centerFrame)

#### END OF INSIDE FRAME ####




#### open Print function FOR PRINT BUTTON ####
def close_print_button():
    print("TEST PRINT CLOSE")
    root.destroy()


def open_print():
    printWindow = Toplevel(root)
    printWindow.title("PRINT")
    printWindow.geometry("500x600+0+0")
    printWindow.resizable(False, False)
    dislpayTitle = Label(printWindow, text="WELCOME TO STORE MANAGEMENT SYSTEM", fg="#31329F", font="Arial 14")
    dislpayTitle.pack(side=TOP)
    displayStaff = Label(printWindow, text="STAFF NAME: "+staffName.get(), fg="#fff", bg="#000")
    displayStaff.pack()
    displayCustomer = Label(printWindow, text="CUSTOMER ID: "+customerId.get(), fg="#fff", bg="#000")
    displayCustomer.pack()
    productNamePrint = Label(printWindow, text="Product Name", fg="#31329F", font="Arial 11")
    productNamePrint.place(x=2, y=80)
    productCodePrint = Label(printWindow, text="Product Code", fg="#31329F", font="Arial 11")
    productCodePrint.place(x=120, y=80)
    productPricePrint = Label(printWindow, text="Price", fg="#31329F", font="Arial 11")
    productPricePrint.place(x=240, y=80)
    productQuantityPrint = Label(printWindow, text="Product Code", fg="#31329F", font="Arial 11")
    productQuantityPrint.place(x=320, y=80)

    ###
    closePrintButton = Button(printWindow, text="CLOSE", bg="#9068be", font="Arial 12", fg="#e1e8f0", padx=14, pady=4, command=close_print_button)
    closePrintButton.pack(side=BOTTOM)

    pointsPrint = Label(printWindow, text="Points: ", fg="#31329F", font="Arial 11")
    pointsPrint.pack(side=BOTTOM)

    totalItemsPrint = Label(printWindow, text="Total Items: ", fg="#31329F", font="Arial 11")
    totalItemsPrint.pack(side=BOTTOM)

    totalPrint = Label(printWindow, text="Total: "+"$", fg="#31329F", font="Arial 11")
    totalPrint.pack(side=BOTTOM)
    print("PRINT TEST")
##### END OF PRINT WINDOW#####

printButton = Button(root, text="PRINT", bg="#9068be", font="Arial 14", fg="#e1e8f0", padx=20, pady=5, command=open_print)
printButton.place(x=40, y=450)


#### CLOSING FUNCTION FOR CLOSE BUTTON ####
def quit(event):
    print("TEST DESTROY")
    root.destroy()


closeButton = Button(root, text="CLOSE", bg="#9068be", font="Arial 14", fg="#e1e8f0", padx=20, pady=5)
closeButton.bind("<Button-1>", quit)
closeButton.place(x=250, y=450)


root.mainloop()