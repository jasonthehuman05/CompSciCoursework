import tkinter
import StockDatabase, CustomerDatabase, StaffDatabase

class CustomerLoginWindow:
    def __init__(self):
        #Public Variables
        
        #Make Window
        self.root = tkinter.Toplevel()
        self.root.geometry("1920x1080") #400x100
        self.root.attributes("-fullscreen", True)
        self.logo = tkinter.PhotoImage(file="logo.png")
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        self.loginFrame = tkinter.Frame(self.root)
        self.loginFrame.place(x=0,y=0,width=1920,height=1080)
        #Logo
        self.imageContainer = tkinter.Label(self.loginFrame, image=self.logo)
        self.imageContainer.place(x=0,y=0)
        #Username stuff
        self.userEntry = tkinter.Entry(self.loginFrame)
        self.userLabel = tkinter.Label(self.loginFrame, text = "USERNAME")
        self.userLabel.place(x=0,y=100)
        #Password Stuff
        self.passEntry = tkinter.Entry(self.loginFrame)
        self.passLabel = tkinter.Label(self.loginFrame, text = "PASSWORD")
        self.passLabel.place(x=0,y=150)
        #Login Button
        self.loginButton = tkinter.Button(self.loginFrame, text="Log In")
        self.loginButton.place(x=0,y=200)




