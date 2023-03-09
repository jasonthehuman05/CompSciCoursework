import tkinter
from tkinter import messagebox
import colorfile
from databases import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, OrderDatabase
import StaffPortal

class StaffLoginScreen:
    def __init__(self, db:StockDatabase.StockDatabase,customerdb:CustomerDatabase.CustomerDB,staffdb:StaffDatabase.StaffDB, bdb:BasketDatabase.BasketDatabase, odb:OrderDatabase.OrderDatabase, openParent):
        #Public vars
        self.db = db
        self.orderdb = odb
        self.customerdb = customerdb
        self.staffdb = staffdb
        self.basketdb = bdb
        self.openParent = openParent
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
        self.openParent()

    def DrawWidgets(self):
        #username
        self.usernameLabel = tkinter.Label(self.root, text="Username")
        self.usernameLabel.place(x=8,y=40,width=92,height=26)
        self.usernameEntry = tkinter.Entry(self.root)
        self.usernameEntry.place(x=100,y=40,width=292,height=26)

        #password
        self.passwordLabel = tkinter.Label(self.root, text="Password")
        self.passwordLabel.place(x=8,y=74,width=92,height=26)
        self.passwordEntry = tkinter.Entry(self.root, show="\u2022")
        self.passwordEntry.place(x=100,y=74,width=292,height=26)

        #Login Button
        self.loginButton = tkinter.Button(self.root, text="Log In", font="default 24 normal", command=lambda:self.TryLogin())
        self.loginButton.place(x=0,y=150,height=50,width=400)

    def TryLogin(self):
        id = self.staffdb.LoginStaff(self.usernameEntry.get(), self.passwordEntry.get())
        if id == "000000":
            messagebox.showwarning("Incorrect Login", "The provided login details could not be found!")
        else:
            self.Login()

        #BYPASS: UNCOMMENT ABOVE AND REMOVE BELOW TO UNBYPASS
        #self.Login()
    
    def Reopen(self):
        self.root.deiconify()

    def Login(self):
        self.root.iconify()
        win = StaffPortal.StaffPortal(self.db, self.customerdb, self.staffdb, self.basketdb, self.orderdb, self.Reopen)
        #self.root.deiconify()



