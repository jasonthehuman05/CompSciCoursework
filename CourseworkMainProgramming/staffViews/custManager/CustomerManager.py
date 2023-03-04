import tkinter
from tkinter import messagebox

class CustomerManager:
    def __init__(self, customerdb, *args):
        #Public Vars
        self.customerdb = customerdb
        self.currentCustomer = ""
        #Create Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Customer Manager")
        self.DrawWidgets()
        self.LoadCustomers()

        #Check if a customer ID was provided
        if len(args) > 0:
            self.DisplayFromCustomerID(args[0])

        self.root.mainloop()

    def DrawWidgets(self):
        #Add Customer Button
        addCustomerButton = tkinter.Button(self.root, text="Add Customer", command=lambda:self.AddCustomer())
        addCustomerButton.grid(row=0,column=0)
        
        #Customer List Box Container
        self.listBoxContainer = tkinter.Frame(self.root)
        self.listBoxContainer.grid(row=1,column=0)

        #Save Changes Button
        self.saveButton = tkinter.Button(self.root, text="", command=lambda: self.DoNothing())
        self.saveButton.grid(row=2,column=1)

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
        self.listBox.delete(0, tkinter.END) # Clear listbox before populating
        #For each customer, add their information
        for customer in self.customerdb.database:
            txt = f"{customer['CustomerID']} {customer['Name']}"
            self.listBox.insert(tkinter.END, txt)

    def DoNothing(self):
        pass

    def AddCustomer(self):
        #Clear all fields
        self.ClearDetails()
        self.idLabel.config(text="New Customer")
        #Update save button
        self.saveButton.config(command=lambda:self.AddNewCustomerToDatabase(), text="Add Customer")

    def AddNewCustomerToDatabase(self):
        #Check Data is valid
        if self.IsDataValid():
            #build new customer
            #Get Data
            name = self.nameBox.get()
            email = self.emailBox.get()
            password = self.passwordBox.get()
            addrl1 = self.addrLine1Box.get()
            addrl2 = self.addrLine2Box.get()
            city = self.cityBox.get()
            postcode = self.postcodeBox.get()
            phoneNumber = self.phoneNumberBox.get()
            self.customerdb.AddCustomer(name, email, password, addrl1, addrl2, city, postcode, phoneNumber)
        #update details
        self.saveButton.config(command=lambda:self.DoNothing(), text="")

    def SaveChanges(self):
        #Check Data is valid
        if self.IsDataValid():
            #update customer
            #Get Data
            name = self.nameBox.get()
            email = self.emailBox.get()
            password = self.passwordBox.get()
            addrl1 = self.addrLine1Box.get()
            addrl2 = self.addrLine2Box.get()
            city = self.cityBox.get()
            postcode = self.postcodeBox.get()
            phoneNumber = self.phoneNumberBox.get()
            
            #Build customer
            data = {
                "CustomerID": self.currentCustomer,
                "Name": name,
                "Email": email,
                "Password": password,
                "AddressLine1": addrl1,
                "AddressLine2": addrl2,
                "City": city,
                "Postcode": postcode,
                "PhoneNumber": phoneNumber
            }

            self.customerdb.SaveCustomer(self.currentCustomer, data)
            messagebox.showinfo("Updated", "Updated customer details!")
        #update details
        self.saveButton.config(command=lambda:self.DoNothing(), text="")
        self.ClearDetails()
        self.LoadCustomers()

    def IsDataValid(self) -> bool:
        valid = True
        #Get Data
        name = self.nameBox.get()
        email = self.emailBox.get()
        addrl1 = self.addrLine1Box.get()
        addrl2 = self.addrLine2Box.get()
        city = self.cityBox.get()
        postcode = self.postcodeBox.get()
        phoneNumber = self.phoneNumberBox.get()

        #Check values
        if len(name) == 0:
            messagebox.showerror("Invalid Input", "Name must be provided")
            valid = False
        
        if "@" not in email:
            messagebox.showerror("Invalid Input", "Incorrect email format")
            valid = False
        
        if len(addrl1) == 0:
            messagebox.showerror("Invalid Input", "Missing address line 1")
            valid = False
        
        if len(city) == 0:
            messagebox.showerror("Invalid Input", "Missing city")
            valid = False
        
        if len(postcode) == 0:
            messagebox.showerror("Invalid Input", "Missing postcode")
            valid = False

        if len(phoneNumber) != 11 or phoneNumber[0] != "0":
            messagebox.showerror("Invalid Input", "Please check phone number")
            valid = False

        return valid

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
        #password
        self.passwordLabel = tkinter.Label(self.informationFrame, text="Password")
        self.passwordBox = tkinter.Entry(self.informationFrame)
        self.passwordLabel.grid(row=3,column=0)
        self.passwordBox.grid(row=3,column=1)
        #Address
        self.addrLine1Label = tkinter.Label(self.informationFrame, text="Address")
        self.addrLine1Box = tkinter.Entry(self.informationFrame)
        self.addrLine1Label.grid(row=4,column=0)
        self.addrLine1Box.grid(row=4,column=1)
        
        self.addrLine2Label = tkinter.Label(self.informationFrame, text="Line 2")
        self.addrLine2Box = tkinter.Entry(self.informationFrame)
        self.addrLine2Label.grid(row=5,column=0)
        self.addrLine2Box.grid(row=5,column=1)

        self.cityLabel = tkinter.Label(self.informationFrame, text="City")
        self.cityBox = tkinter.Entry(self.informationFrame)
        self.cityLabel.grid(row=6,column=0)
        self.cityBox.grid(row=6,column=1)

        self.postcodeLabel = tkinter.Label(self.informationFrame, text="Postcode")
        self.postcodeBox = tkinter.Entry(self.informationFrame)
        self.postcodeLabel.grid(row=7,column=0)
        self.postcodeBox.grid(row=7,column=1)
        
        #Phone Number
        self.phoneNumberLabel = tkinter.Label(self.informationFrame, text="Phone Number")
        self.phoneNumberBox = tkinter.Entry(self.informationFrame)
        self.phoneNumberLabel.grid(row=8,column=0)
        self.phoneNumberBox.grid(row=8,column=1)

    def ClearDetails(self):
        self.idLabel.config(text="Select a customer!")
        self.nameBox.delete(0,tkinter.END)
        self.emailBox.delete(0,tkinter.END)
        self.passwordBox.delete(0, tkinter.END)
        self.addrLine1Box.delete(0,tkinter.END)
        self.addrLine2Box.delete(0,tkinter.END)
        self.cityBox.delete(0,tkinter.END)
        self.postcodeBox.delete(0,tkinter.END)
        self.phoneNumberBox.delete(0,tkinter.END)

        self.saveButton.config(command=lambda:self.DoNothing())
        self.currentCustomer = ""

    def DisplayDetails(self):
        self.ClearDetails()
        self.saveButton.config(command=lambda:self.SaveChanges())
        cid = self.listBox.get(self.listBox.curselection()[0]).split(" ")[0] #Get ID from the selected item

        cd = self.customerdb.GetCustomer(cid) #Get the customer's details from database

        self.idLabel.config(text=f"ID: {cd['CustomerID']}")

        self.nameBox.insert(0,cd["Name"])
        self.emailBox.insert(0, cd["Email"])
        self.addrLine1Box.insert(0, cd["AddressLine1"])
        self.addrLine2Box.insert(0, cd["AddressLine2"])
        self.cityBox.insert(0, cd["City"])
        self.postcodeBox.insert(0, cd["Postcode"])
        self.phoneNumberBox.insert(0, cd["PhoneNumber"])

        self.currentCustomer = cd["CustomerID"]
        self.saveButton.config(text="Save Changes")

    def DisplayFromCustomerID(self, cid:str):
        self.ClearDetails()
        self.saveButton.config(command=lambda:self.SaveChanges())

        cd = self.customerdb.GetCustomer(cid) #Get the customer's details from database

        self.idLabel.config(text=f"ID: {cd['CustomerID']}")

        self.nameBox.insert(0,cd["Name"])
        self.emailBox.insert(0, cd["Email"])
        self.addrLine1Box.insert(0, cd["AddressLine1"])
        self.addrLine2Box.insert(0, cd["AddressLine2"])
        self.cityBox.insert(0, cd["City"])
        self.postcodeBox.insert(0, cd["Postcode"])
        self.phoneNumberBox.insert(0, cd["PhoneNumber"])

        self.currentCustomer = cd["CustomerID"]
        self.saveButton.config(text="Save Changes")