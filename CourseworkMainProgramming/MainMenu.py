import tkinter
import StockDatabase

class MainMenu:
	def __init__(self, db:StockDatabase.StockDatabase):
		#Make vars accessible
		self.userName = "Not Logged In"
		self.db = db
		self.itemDetailHolders = []
		self.activeItemIndexes = []
		#Make Window
		self.root = tkinter.Tk()
		self.root.attributes('-fullscreen', True)
		self.root.title("BuildrightDB")
		self.DrawWidgets()
		self.root.mainloop()
	
	def ShowWindow(self):
		self.root.deiconify()

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
		self.searchButton = tkinter.Button(self.root, text="SEARCH", font = "default 16 normal", command=lambda:self.MakeSearch())
		self.searchButton.place(x=1184,y=8,width=100,height=48)

		#Body Frame
		self.bodyFrame = tkinter.Frame(self.root, bg="CadetBlue4")
		self.bodyFrame.place(x=0,y=64,width=1920,height=1016)

		#Stock Frame
		self.stockInfoFrame = tkinter.Frame(self.bodyFrame,bg="CadetBlue1")
		self.stockInfoFrame.place(x=256,y=0,width=1664,height=1016)
		self.DrawItemHolders()
	
	def DrawItemHolders(self):		
		#Variables for sizing
		padding = 8
		objHeight = 128

		#Generate item info
		for i in range(0,7):
			#Containing Frame
			self.itemDetailHolders.append(tkinter.Frame(self.stockInfoFrame))
			self.itemDetailHolders[i].place(x=8,y=padding+((padding+objHeight)*i),width=1648,height=objHeight)
			
			#View Button
			detailsButton = tkinter.Button(self.itemDetailHolders[i], text="View Details", font = "default 24 normal")
			detailsButton.place(x=1376, y=16, width=256, height=96)

	def MakeSearch(self):
		self.activeItemIndexes = self.db.SearchForItem(self.searchBar.get())
		self.DrawProducts()

	def DrawProducts(self):
		pass

		

