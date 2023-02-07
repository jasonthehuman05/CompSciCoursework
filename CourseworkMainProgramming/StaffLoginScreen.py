import tkinter
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase
import StaffPortal

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
        self.root.protocol("WM_DELETE_WINDOW", self.HandleClose) #Captures the close event to close it properly
        self.DrawWidgets()
        self.root.mainloop()

    def HandleClose(self):
        self.root.quit()
        self.root.destroy()

    def DrawWidgets(self):
        #Login Button
        self.loginButton = tkinter.Button(self.root, text="Log In", font="default 24 normal", command=lambda:self.TryLogin())
        self.loginButton.place(x=0,y=150,height=50,width=400)

    def TryLogin(self):
        self.Login()
    
    def Login(self):
        self.root.withdraw()
        win = StaffPortal.StaffPortal(self.db, self.customerdb, self.staffdb, self.basketdb, self.orderdb)
        self.root.deiconify()



