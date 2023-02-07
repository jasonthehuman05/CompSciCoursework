import tkinter
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase

class StaffLoginScreen:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase, odb:OrderDatabase.OrderDatabase):
        #Public vars
        self.db = db
        self.orderdb = odb
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb

        #Window Builder
        self.root = tkinter.Toplevel()
        self.root.title("BuildrightDB Staff Login")
        self.root.geometry("400x200")
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        pass




