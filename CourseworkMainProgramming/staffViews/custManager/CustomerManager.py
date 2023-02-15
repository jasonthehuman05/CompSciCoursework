import tkinter
from turtle import width

class CustomerManager:
    def __init__(self, customerdb):
        #Public Vars
        self.customerdb = customerdb

        #Create Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Customer Manager")
        self.DrawWidgets()

    def DrawWidgets(self):
        #Add Customer Button
        addCustomerButton = tkinter.Button(self.root, text="Add Customer", command=lambda:self.AddCustomer())
        addCustomerButton.grid(row=0,column=0)
        
        #Customer List Box Container
        self.listBoxContainer = tkinter.Frame(self.root)
        self.listBoxContainer.grid(row=1,column=0)

        #Listbox and scrollbar
        self.listBox = tkinter.Listbox(self.listBoxContainer)
        self.listBox.pack(side="left", fill="y")
        self.lbScrollbar = tkinter.Scrollbar(self.listBoxContainer, orient="vertical")
        self.listBox.config(yscrollcommand=self.lbScrollbar.set)
        self.lbScrollbar.pack(side="right", fill="y")

        #Open Button
        self.openDetailsButton = tkinter.Button(self.root, text="Open Customer", command=lambda:self.DisplayDetails())
        self.openDetailsButton.grid(column=0,row=2)

        #Information Holder
        self.informationFrame = tkinter.Frame(self.root, bg="#ffffff", width=100)
        self.informationFrame.grid(row=0,column=1, rowspan=2)
        self.DrawDetailsHolder()
       
    def LoadCustomers(self):
        pass

    def AddCustomer(self):
        pass

    def DrawDetailsHolder(self):
        #ID
        self.idLabel = tkinter.Label(self.informationFrame, text="Select a customer!")
        self.idLabel.grid(column=0,row=0,columnspan=2)
        #Name
        self.nameLabel = tkinter.Label(self.informationFrame, text="Name")
        self.nameBox = tkinter.Entry(self.informationFrame)
        self.nameLabel.grid(row=1,column=0)
        self.nameBox.grid(row=1,column=1)
        #Email
        self.emailLabel = tkinter.Label(self.informationFrame, text="Email")
        self.emailBox = tkinter.Entry(self.informationFrame)
        self.emailLabel.grid(row=2,column=0)
        self.emailBox.grid(row=2,column=1)
        #Address
        self.addrLine1Label = tkinter.Label(self.informationFrame, text="Address")
        self.addrLine1Box = tkinter.Entry(self.informationFrame)
        self.addrLine1Label.grid(row=3,column=0)
        self.addrLine1Box.grid(row=3,column=1)
        
        self.addrLine2Label = tkinter.Label(self.informationFrame, text="Line 2")
        self.addrLine2Box = tkinter.Entry(self.informationFrame)
        self.addrLine2Label.grid(row=4,column=0)
        self.addrLine2Box.grid(row=4,column=1)

        self.cityLabel = tkinter.Label(self.informationFrame, text="City")
        self.cityBox = tkinter.Entry(self.informationFrame)
        self.cityLabel.grid(row=5,column=0)
        self.cityBox.grid(row=5,column=1)

        self.postcodeLabel = tkinter.Label(self.informationFrame, text="Postcode")
        self.postcodeBox = tkinter.Entry(self.informationFrame)
        self.postcodeLabel.grid(row=6,column=0)
        self.postcodeBox.grid(row=6,column=1)
        
        #Phone Number
        self.phoneNumberLabel = tkinter.Label(self.informationFrame, text="Phone Number")
        self.phoneNumberBox = tkinter.Entry(self.informationFrame)
        self.phoneNumberLabel.grid(row=7,column=0)
        self.phoneNumberBox.grid(row=7,column=1)

    def ClearDetails(self):
        self.idLabel.config(text="Select a customer!")
        self.nameBox.delete(0,tkinter.END)
        self.emailBox.delete(0,tkinter.END)
        self.addrLine1Box.delete(0,tkinter.END)
        self.addrLine2Box.delete(0,tkinter.END)
        self.cityBox.delete(0,tkinter.END)
        self.postcodeBox.delete(0,tkinter.END)
        self.phoneNumberBox.delete(0,tkinter.END)

    def DisplayDetails(self):
        cid = self.listBox.curselection()[0] #Get the selected item

        cd = self.customerdb.GetCustomer(cid) #Get the customer's details from database

        self.idLabel.config(text=f"ID: {cd['CustomerID']}")

        self.nameBox.insert(0,cd["name"])
        self.emailBox.insert(0, cd["Email"])
        self.addrLine1Box.insert(0, cd["addressLine1"])
        self.addrLine2Box.insert(0, cd["addressLine2"])
        self.cityBox.insert(0, cd["City"])
        self.postcodeBox.insert(0, cd["Postcode"])
        self.phoneNumberBox.insert(0, cd["Postcode"])