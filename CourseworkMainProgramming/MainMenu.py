import tkinter
import math
import StockDatabase
class MainMenu:
	def __init__(self, db:StockDatabase.StockDatabase):
		#Make vars accessible
		self.objHeight = 128
		self.userName = "Not Logged In"
		self.db = db

		#Controls for item details
		self.itemDetailHolders = []
		self.itemDetailHoldersPositions = []
		self.ViewButtons = []
		self.prodNumLabels = []
		self.prodNameLabels = []

		self.activeItemIndexes = []
		self.pageCount = 0

		#Make Window
		self.root = tkinter.Tk()
		self.root.attributes('-fullscreen', True) #Makes the window appear in fullscreen mode.
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
		self.GenerateItemHolders()
		#Page Navigation
		self.pageNavFrame = tkinter.Frame(self.stockInfoFrame, bg="CadetBlue3")
		self.pageNavFrame.place(x=0,y=956,width=1664,height=60)

		self.prevPageButton = tkinter.Button(self.pageNavFrame, text="⬅", font = "default 24 normal")
		self.prevPageButton.place(x=8,y=8,width=200,height=44)

		self.pageNumberLabel = tkinter.Label(self.pageNavFrame, text="Page 1 of 1", font = "default 16 normal", bg="CadetBlue3")
		self.pageNumberLabel.place(x=732,y=8,height=44,width=200)

		self.nextPageButton = tkinter.Button(self.pageNavFrame, text="➡", font = "default 24 normal")
		self.nextPageButton.place(x=1456,y=8,width=200,height=44)
	
	def GenerateItemHolders(self):		
		#Variables for sizing
		padding = 8
		self.objHeight = 128

		#Generate item info
		for i in range(0,7):
			#Containing Frame
			self.itemDetailHolders.append(tkinter.Frame(self.stockInfoFrame, bg="gray60"))
			self.itemDetailHoldersPositions.append(padding+((padding+self.objHeight)*i)) #Calculate Y position

			self.itemDetailHolders[i].place(x=8,y=self.itemDetailHoldersPositions[i],width=1648,height=self.objHeight)
			
			#View Button
			self.ViewButtons.append(tkinter.Button(self.itemDetailHolders[i], text="View Details", font = "default 24 normal"))
			self.ViewButtons[i].place(x=1376, y=16, width=256, height=96)

			#product number label
			self.prodNumLabels.append(tkinter.Label(self.itemDetailHolders[i], text="000000", font = "default 16 normal", anchor="w", bg="gray60"))
			self.prodNumLabels[i].place(x=8, y=94, width=1000)

			#product name label
			self.prodNameLabels.append(tkinter.Label(self.itemDetailHolders[i], text="SAMPLE TEXT", font = "default 32 normal", anchor="w", bg="gray60"))
			self.prodNameLabels[i].place(x=8, y=8, width=1200, height = 82)

			#Hide all containers. they aren't needed, so they should be removed to avoid confusion
			for searchIndex in range(0,7):
				self.itemDetailHolders[searchIndex].place_forget()



	def MakeSearch(self):
		#Get Items
		self.activeItemIndexes = self.db.SearchForItem(self.searchBar.get())

		#Calculate number of pages
		self.pageCount = math.ceil(len(self.activeItemIndexes) / 7)

		self.DrawProducts(0)

	def ShowDetails(self, prodNum:str):
		print(prodNum)

	def DrawProducts(self, startingIndex:int):
		#Hide all containers
		for searchIndex in range(0,7):
			self.itemDetailHolders[searchIndex].place_forget()

		endIndex = startingIndex+7
		if len(self.activeItemIndexes)-1 < endIndex:
			endIndex = len(self.activeItemIndexes)-1

		elementIndex = 0
		for searchIndex in range(startingIndex, endIndex+1):
			item = self.db.database["items"][self.activeItemIndexes[searchIndex]] #Get the item to display
			print(item["productNumber"])
			#Draw the item container
			self.itemDetailHolders[elementIndex].place(x=8,y=self.itemDetailHoldersPositions[elementIndex],width=1648,height=self.objHeight)
			#Redo the button and labels
			self.ViewButtons[elementIndex].configure(command=lambda x=item["productNumber"]: self.ShowDetails(x))
			self.prodNameLabels[elementIndex].configure(text=item["productName"])
			self.prodNumLabels[elementIndex].configure(text=f"Item Number: {item['productNumber']}")
			#Increment Element
			elementIndex+=1