import tkinter
import CustomerLoginWindow, StaffPortal, StaffLoginScreen
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase

class MainMenu:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase, odb:OrderDatabase.OrderDatabase):
        #Public vars
        self.db = db
        self.orderdb = odb
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb
        #Create Window
        self.root = tkinter.Tk()

        self.logo = tkinter.PhotoImage(file="logo-small.png")

        self.root.title("BuildrightDB - Select An Option")
        self.root.configure(bg=colorfile.accent[0])
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

        #Option Buttons
        buttonHeight = 64
        self.openCustomerButton = tkinter.Button(self.root, text="Customer Portal", font ="default 36 normal", command = lambda:self.OpenCustomerView())
        self.openCustomerButton.place(x=150,y=193, width=600,height=buttonHeight)
        self.openStaffButton = tkinter.Button(self.root, text="Staff Portal", font ="default 36 normal", command= lambda:self.OpenStaffPortal())
        self.openStaffButton.place(x=150,y=265, width=600,height=buttonHeight)

    def HideWindow(self):
        self.root.iconify()

    def ShowWindow(self):
        try:
            self.root.deiconify()
        except: pass

    def OpenCustomerView(self):
        self.HideWindow()
        cv = CustomerLoginWindow.CustomerLoginWindow(self.db,self.customerdb,self.basketdb)
        self.ShowWindow()

    def OpenStaffPortal(self): #This needs to go to staff login page!!!!!
        self.HideWindow()
        StaffLoginScreen.StaffLoginScreen(self.db, self.customerdb, self.staffdb, self.basketdb, self.orderdb, lambda:self.root.deiconify())
        self.ShowWindow()