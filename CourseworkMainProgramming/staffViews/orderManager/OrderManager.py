import tkinter
from turtle import width
from databases import OrderDatabase

class OrderManager:
    def __init__(self, odb:OrderDatabase.OrderDatabase):
        #Public Vars
        self.orderdb = odb

        #Make Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Orders")
        self.root.geometry("500x285")
        
        self.DrawWidgets()
        self.root.mainloop()

            
    def DrawWidgets(self):
        #Orders and Details Container
        self.orderContainer = tkinter.Frame(self.root)
        self.detailsContainer = tkinter.Frame(self.root)
        self.orderContainer.grid(row=0,column=0)
        self.detailsContainer.grid(row=0,column=1,columnspan=2)

        #Order list box
        self.orderListBox = tkinter.Listbox(self.orderContainer, width=37,height=16)
        self.orderScrollbar = tkinter.Scrollbar(self.orderContainer, orient="vertical")

        self.orderListBox.pack(side="left", fill="y")
        self.orderListBox.config(yscrollcommand=self.orderScrollbar.set)
        self.orderScrollbar.pack(side="right", fill="y")

        #Order details list box
        self.detailsListBox = tkinter.Listbox(self.detailsContainer, width=37,height=16)
        self.detailsScrollbar = tkinter.Scrollbar(self.detailsContainer, orient="vertical")

        self.detailsListBox.pack(side="left", fill="y")
        self.detailsListBox.config(yscrollcommand=self.detailsScrollbar.set)
        self.detailsScrollbar.pack(side="right", fill="y")

        #Open Order Button
        self.openOrderButton = tkinter.Button(self.root, text="Open Selected", command=lambda:self.OpenOrder())
        self.openOrderButton.grid(row=1,column=0, sticky="nesw")

        #Open Customer Button
        self.openCustomerButton = tkinter.Button(self.root, text="Open Customer Details", command=lambda:self.OpenCustomerDetails())
        self.openCustomerButton.grid(row=1,column=1, sticky="nesw")

        #Close Order Button
        self.closeOrderButton = tkinter.Button(self.root, text="Close Order", command=lambda:self.CompleteOrder())
        self.closeOrderButton.grid(row=1,column=2, sticky="nesw")

    def OpenOrder(self):
        pass

    def OpenCustomerDetails(self):
        pass

    def CompleteOrder(self):
        pass