import tkinter
import CustomerLoginWindow
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase
from staffViews.stockManager import StockManager
from staffViews.staffManager import StaffManager
from staffViews.custManager import CustomerManager

class StaffPortal:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase, odb:OrderDatabase.OrderDatabase, closeFn):
        #Public vars
        self.db = db
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb
        self.closeFn = closeFn
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

        #Stock Management
        self.stockViewButton = tkinter.Button(self.root, text="Stock Management", command=lambda:self.ViewStock())
        self.stockViewButton.place(x=8,y=100,width=438,height=125)

        #Staff Management
        self.staffViewButton = tkinter.Button(self.root, text="Staff Management", command=lambda:self.ViewStaff())
        self.staffViewButton.place(x=454,y=100,width=438,height=125)

        #Customer Management
        self.customerViewButton = tkinter.Button(self.root, text="Customer Management", command=lambda:self.ViewCustomer())
        self.customerViewButton.place(x=8,y=233,width=438,height=125)

        #Order Management
        self.orderViewButton = tkinter.Button(self.root, text="Order Management", command=lambda:self.ViewOrder())
        self.orderViewButton.place(x=454,y=233,width=438,height=125)

    def HandleClose(self):
        #print("Closing!")
        self.root.quit()
        self.root.destroy()
        self.closeFn()

    def ViewStock(self):
        stockmm = StockManager.StockManager(self.db)

    def ViewStaff(self):
        staffm = StaffManager.StaffManager(self.staffdb)
    
    def ViewCustomer(self):
        cman = CustomerManager.CustomerManager(self.customerdb)

    def ViewOrder(self):
        pass