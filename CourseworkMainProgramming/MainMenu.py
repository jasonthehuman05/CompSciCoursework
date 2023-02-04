import tkinter
import CustomerLoginWindow
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase
class MainMenu:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase):
        #Public vars
        self.db = db
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb
        #Create Window
        self.root = tkinter.Tk()
        self.root.title("BuildrightDB")
        self.root.geometry("900x450")
        self.DrawWidgets()

        self.root.mainloop()

    def DrawWidgets(self):
        pass

    def OpenCustomerView(self):
        cv = CustomerLoginWindow.CustomerLoginWindow(self.db,self.customerdb,self.staffdb,self.bdb)



