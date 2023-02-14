import tkinter

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

        #Information Holder
        self.informationFrame = tkinter.Frame(self.root, bg="#ffffff")
        self.informationFrame.grid(row=0,column=1, rowspan=1)
        
    def AddCustomer(self):
        pass




