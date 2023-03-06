import tkinter
from tkinter import messagebox
from databases import OrderDatabase, CustomerDatabase, StockDatabase
from staffViews.custManager import CustomerManager

class OrderManager:
    def __init__(self, odb:OrderDatabase.OrderDatabase, cdb:CustomerDatabase.CustomerDB, sdb:StockDatabase.StockDatabase):
        #Public Vars
        self.orderdb = odb
        self.customerdb = cdb
        self.stockdb = sdb
        self.orderNumber = ""

        #Make Window
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Orders")
        self.root.geometry("650x285")
        
        self.DrawWidgets()
        self.DisplayOrders()
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
        self.detailsListBox = tkinter.Listbox(self.detailsContainer, width=64,height=16)
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

    def DisplayOrders(self):
        #Get all orders
        orders = self.orderdb.database
        
        #For each order, add it to the list box
        for order in orders:
            #get customer details
            customer = self.customerdb.GetCustomer(order["CustomerID"])
            #Build string to display
            lboxString = f"{order['OrderID']} :: {customer['Name']}"
            self.orderListBox.insert("end", lboxString)


    def OpenOrder(self):
        self.ClearOrderDetails()

        try:
            #Get order number
            self.orderNumber = self.orderListBox.get(self.orderListBox.curselection()[0]).split(" :: ")[0] #Get ID from the selected item
        
            #Get order details
            order = self.orderdb.GetOrder(self.orderNumber)
            products = order["Items"]

            #For each product, get its details and add it to the listbox
            for item in products:
                pnum = item["ProductID"].split(":")[0]
                sitem = self.stockdb.GetItemByProductNumber(pnum)
                variation = self.stockdb.GetVariation(item["ProductID"])
                boxString = f"{item['Count']}x {sitem['productName']} :: {variation['variationName']}"

                self.detailsListBox.insert("end", boxString)

        except: return

    def ClearOrderDetails(self):
        self.detailsListBox.delete(0, "end")
        
    def ClearOrderList(self):
        self.orderListBox.delete(0, "end")

    def OpenCustomerDetails(self):
        try:
            #Find customer number
            order = self.orderdb.GetOrder(self.orderNumber)
            customerID = order["CustomerID"]
            #Open details
            cman = CustomerManager.CustomerManager(self.customerdb, customerID)
            cman.DisplayFromCustomerID(customerID)
        except :
            return

    def CompleteOrder(self):
        try:
            completeOrder = messagebox.askyesno("Complete Order", "Would you like to close this order? This cannot be reversed.")
            
            if completeOrder:
                #delete from orders list
                self.orderdb.DeleteOrder(self.orderNumber)
            
                #refresh display
                self.ClearOrderDetails()
                self.ClearOrderList()
                self.orderNumber = ""
        except: return