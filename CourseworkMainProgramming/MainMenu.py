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

        self.logo = tkinter.PhotoImage(file="logo-small.png")

        self.root.title("BuildrightDB")
        self.root.geometry("900x450")
        self.DrawWidgets()

        self.root.mainloop()

    def DrawWidgets(self):
        #Header Frame
        self.headerFrame = tkinter.Frame(self.root, bg=colorfile.container)
        self.headerFrame.place(x=0,y=0,width=900,height=64)
        #Logo Label
        self.imageContainer = tkinter.Label(self.headerFrame, image=self.logo, bg=colorfile.container)
        self.imageContainer.place(x=8,y=4)

    def OpenCustomerView(self):
        cv = CustomerLoginWindow.CustomerLoginWindow(self.db,self.customerdb,self.staffdb,self.bdb)



