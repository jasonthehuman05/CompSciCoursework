import tkinter
import CustomerLoginWindow
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase

class StaffPortal:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase, odb:OrderDatabase.OrderDatabase):
        #Public vars
        self.db = db
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb

        #Window Builder
        self.root = tkinter.Toplevel()
        self.root.protocol("WM_DELETE_WINDOW", self.HandleClose) #Captures the close event to close it properly
        self.root.title("BuildrightDB")
        self.root.geometry("900x450")
        self.DrawWidgets()

        self.root.mainloop()

    def DrawWidgets(self):
        #Header Frame
        self.headerFrame = tkinter.Frame(self.root, bg=colorfile.container)
        self.headerFrame.place(x=0,y=0,width=900,height=64)
        self.titleLabel = tkinter.Label(self.headerFrame, text="Staff Portal")

    def HandleClose(self):
        self.root.quit()
        self.root.destroy()