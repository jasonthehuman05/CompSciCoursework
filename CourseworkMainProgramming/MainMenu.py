import tkinter
import StockDatabase

class MainMenu:
	def __init__(self, userName = "Not Logged In"):
		#Make vars accessible
		self.userName = userName

		#Make Window
		self.root = tkinter.Tk()
		self.root.attributes('-fullscreen', True)
		self.root.title("BuildrightDB")
		self.DrawWidgets()
		self.root.mainloop()
	
	def DrawWidgets(self):
		#Main Header Frame
		fbg="orange red"
		self.headerFrame = tkinter.Frame(self.root, bg=fbg)
		self.headerFrame .place(x=0,y=0,width=1920,height=64)

		#Account Information
		self.greetingLabel = tkinter.Label(self.headerFrame, text=f"Hello, {self.userName}", bg=fbg, fg="white")
		self.greetingLabel.place(x=8,y=8,height=24)
		self.logoutButton = tkinter.Button(self.headerFrame, text="Log Out")
		self.logoutButton.place(x=8,y=32,height=24,width=100, anchor="nw")

		#Searching
		self.searchBar = tkinter.Entry(self.root, font = "default 28 normal")
		self.searchBar.place(x=536,y=8,width=640,height=48)
		self.searchButton = tkinter.Button(self.root, text="SEARCH", font = "default 16 normal")
		self.searchButton.place(x=1184,y=8,width=100,height=48)

		#Body Frame
		self.bodyFrame = tkinter.Frame(self.root, bg="CadetBlue4")
		self.bodyFrame.place(x=0,y=64,width=1920,height=1016)

		#Stock Frame
		self.stockInfoFrame = tkinter.Frame(self.bodyFrame,bg="CadetBlue1")
		self.stockInfoFrame.place(x=256,y=0,width=1664,height=1016)
		
	def ShowWindow(self):
		self.root.deiconify()



