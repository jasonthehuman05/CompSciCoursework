import tkinter
import colorfile
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
        self.loginFrame = tkinter.Frame(self.root, bg=colorfile.topbarcolor)
        self.loginFrame.place(x=752,y=416,width=416,height=248)
        #Logo
        self.imageContainer = tkinter.Label(self.loginFrame, image=self.logo, bg=colorfile.topbarcolor)
        self.imageContainer.place(x=8,y=8)
        #Username stuff
        self.userEntry = tkinter.Entry(self.loginFrame, font="default 14 normal")
        self.userLabel = tkinter.Label(self.loginFrame, text = "USERNAME", font="default 14 normal", bg=colorfile.topbarcolor)
        self.userLabel.place(x=8,y=112)
        self.userEntry.place(x=128,y=108,width=280,height=40)
        #Password Stuff
        self.passEntry = tkinter.Entry(self.loginFrame, font="default 14 normal")
        self.passLabel = tkinter.Label(self.loginFrame, text = "PASSWORD", font="default 14 normal", bg=colorfile.topbarcolor)
        self.passLabel.place(x=8,y=158)
        self.passEntry.place(x=128,y=153,width=280,height=40)
        #Login Button
        self.loginButton = tkinter.Button(self.loginFrame, text="Log In")
        self.loginButton.place(x=8,y=208,width=400,height=32)




