import tkinter
import CustomerLoginWindow
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase
from staffViews.stockManager import StockManager

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
        self.headerFrame = tkinter.Frame(self.root, bg=colorfile.topbarcolor)
        self.headerFrame.place(x=0,y=0,width=900,height=64)
        self.titleLabel = tkinter.Label(self.headerFrame, text="Staff Portal", font="default 32 normal", anchor="w", bg=colorfile.topbarcolor)
        self.titleLabel.place(x=8,y=8,width=400,height=48)

        self.stockViewButton = tkinter.Button(self.root, text="Stock Management", command=lambda:self.ViewStock())
        self.stockViewButton.place(x=8,y=100,width=438,height=125)

    def HandleClose(self):
        self.root.quit()
        self.root.destroy()

    def ViewStock(self):
        sm = StockManager.StockManager(self.db)