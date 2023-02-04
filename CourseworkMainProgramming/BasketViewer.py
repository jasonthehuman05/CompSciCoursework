from tkinter import messagebox
import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase, colorfile
import MainCustomerScreen
import tkinter, math

class BasketViewer:
	def __init__(self, db:StockDatabase.StockDatabase, cdb:CustomerDatabase.CustomerDB, bdb:BasketDatabase.BasketDatabase, cid:str):
		#Public Vars
		self.db = db
		self.customerdb = cdb
		self.basketdb = bdb
		self.userid = cid
		self.itemDetailHolders = []
		
		#Controls for item details
		self.itemDetailHolders = []
		self.itemDetailHoldersPositions = []
		self.prodNumLabels = []
		self.varNameLabels = []
		self.prodNameLabels = []
		self.subtractItemButton = []
		self.addItemButton = []
		self.itemCountLabel = []


		self.basket = []
		self.pageCount = 0
		self.currentPage = 1
		#Window Creation
		self.root = tkinter.Toplevel()
		self.root.title("Basket View")
		self.root.geometry("1920x1080")
		self.root.attributes("-fullscreen", True)
		self.DrawWidgets()
		self.root.after(500, self.LoadItems)
		self.root.mainloop()
    
	def ShowWindow(self):
		self.root.deiconify()

	def Filter(self, tag:str):
		self.searchBar.delete(0, 'end')
		self.searchBar.insert(0, tag)
		self.LoadItems()

	def DrawWidgets(self):
		#Main Header Frame
		fbg=colorfile.topbarcolor
		self.headerFrame = tkinter.Frame(self.root, bg=fbg)
		self.headerFrame .place(x=0,y=0,width=1920,height=64)

		#Basket
		self.basketButton = tkinter.Button(self.headerFrame, text="PLACE ORDER", command=lambda:self.PlaceOrder())
		self.basketButton.place(x=1800,y=8,width=114,height=48)

		#Back Button
		self.logoutButton = tkinter.Button(self.headerFrame, text="Return", command=lambda:self.Return())
		self.logoutButton.place(x=8,y=8,height=48,width=100, anchor="nw")

		#Header Label
		self.searchBar = tkinter.Label(self.root, text="BASKET", font = "default 28 normal", bg=colorfile.topbarcolor)
		self.searchBar.place(x=636,y=8,width=640,height=48)

		#Body Frame
		self.bodyFrame = tkinter.Frame(self.root, bg=colorfile.accent[3])
		self.bodyFrame.place(x=0,y=64,width=1920,height=1016)

		#Stock Frame
		self.stockInfoFrame = tkinter.Frame(self.bodyFrame,bg=colorfile.accent[0])
		self.stockInfoFrame.place(x=0,y=0,width=1920,height=1016)
		self.GenerateItemHolders()

		#Page Navigation
		self.pageNavFrame = tkinter.Frame(self.stockInfoFrame, bg=colorfile.accent[2])
		self.pageNavFrame.place(x=0,y=956,width=1920,height=60)

		self.prevPageButton = tkinter.Button(self.pageNavFrame, text="⬅", font = "default 24 normal", command=lambda:self.ChangePage(-1))
		self.prevPageButton.place(x=8,y=8,width=200,height=44)

		self.pageNumberLabel = tkinter.Label(self.pageNavFrame, text="Page 1 of 1", font = "default 16 normal", bg=colorfile.accent[2])
		self.pageNumberLabel.place(x=218,y=8,height=44,width=1505)

		self.nextPageButton = tkinter.Button(self.pageNavFrame, text="➡", font = "default 24 normal", command=lambda:self.ChangePage(1))
		self.nextPageButton.place(x=1712,y=8,width=200,height=44)

	def PlaceOrder(self):
		pass

	def Return(self):
		self.root.quit()
		self.root.destroy()

	def GenerateItemHolders(self):		
		#Variables for sizing
		padding = 8
		self.objHeight = 128

		#Generate item info
		for i in range(0,7):
			#Containing Frame
			self.itemDetailHolders.append(tkinter.Frame(self.stockInfoFrame, bg=colorfile.container))
			self.itemDetailHoldersPositions.append(padding+((padding+self.objHeight)*i)) #Calculate Y position

			self.itemDetailHolders[i].place(x=8,y=self.itemDetailHoldersPositions[i],width=1904,height=self.objHeight)
			
			#product name label
			self.prodNameLabels.append(tkinter.Label(self.itemDetailHolders[i], text="SAMPLE TEXT", font = "default 32 normal", anchor="w", bg=colorfile.container))
			self.prodNameLabels[i].place(x=8, y=8, width=1200, height = 66)
			#variation name label
			self.varNameLabels.append(tkinter.Label(self.itemDetailHolders[i], text="Variation Goes Here", font = "default 20 normal", anchor="w", bg=colorfile.container))
			self.varNameLabels[i].place(x=8, y=60, width=1000)
			#product number label
			self.prodNumLabels.append(tkinter.Label(self.itemDetailHolders[i], text="000000", font = "default 14 normal", anchor="w", bg=colorfile.container))
			self.prodNumLabels[i].place(x=8, y=96, width=1000)

			#Item count and add/rem buttons
			self.subtractItemButton.append(tkinter.Button(self.itemDetailHolders[i], text="-", font="default 36 normal"))
			self.addItemButton.append(tkinter.Button(self.itemDetailHolders[i], text="+", font="default 36 normal"))
			self.itemCountLabel.append(tkinter.Label(self.itemDetailHolders[i], text="88", font="default 24 normal",bg=colorfile.container))

			self.addItemButton[i].place(x=1784, y=8, width=112)
			self.subtractItemButton[i].place(x=1512, y=8, width=112)
			self.itemCountLabel[i].place(x=1648, y=8, width=112,height=112)


		#Hide all containers. they aren't needed, so they should be removed to avoid confusion
		for searchIndex in range(0,7):
			self.itemDetailHolders[searchIndex].place_forget()



	def LoadItems(self):
		#Get Basket
		self.basket = self.basketdb.GetBasket(self.userid)

		#Calculate number of pages
		self.pageCount = math.ceil(len(self.basket) / 7)
		self.pageNumberLabel.configure(text=f"Page {self.currentPage} of {self.pageCount}")

		#Displays items from the basket
		self.DisplayItems(0)

	def ChangePage(self, delta:int):#Go delta pages in direction
		nPageNum = self.currentPage + delta
		if nPageNum > self.pageCount or nPageNum < 1: #Out of range, ignore command
			return
		else:
			#Make the change
			self.currentPage = nPageNum
			self.DisplayItems((self.currentPage-1) * 7) #Display items starting at the correct index in the basket

	#All test items: nails mounting home wood outdoor pipe

	def DisplayItems(self, startingIndex:int):
		#Set Page Indicator
		self.pageNumberLabel.configure(text=f"Page {self.currentPage} of {self.pageCount}")
		
		#Hide all containers
		for searchIndex in range(0,7):
			self.itemDetailHolders[searchIndex].place_forget()

		endIndex = startingIndex+7
		if len(self.basket)-1 < endIndex:
			endIndex = len(self.basket)

		elementIndex = 0
		for searchIndex in range(startingIndex, endIndex):
			item = self.db.GetItemByProductNumber(self.basket[searchIndex]["ProductID"].split(":")[0]) #Get the actual item
			variation = self.db.GetVariation(self.basket[searchIndex]["ProductID"])

			#Draw the item container
			self.itemDetailHolders[elementIndex].place(x=8,y=self.itemDetailHoldersPositions[elementIndex],width=1904,height=self.objHeight)
			#Redo the button and labels
			self.prodNameLabels[elementIndex].configure(text=item["productName"])
			self.varNameLabels[elementIndex].configure(text=variation["variationName"])
			self.prodNumLabels[elementIndex].configure(text=f"Item Variation: {self.basket[searchIndex]['ProductID']}")

			self.addItemButton[elementIndex].configure(command=lambda ind = elementIndex: self.ChangeItemCount(ind, 1))
			self.subtractItemButton[elementIndex].configure(command=lambda ind = elementIndex: self.ChangeItemCount(ind, -1))
			self.itemCountLabel[elementIndex].configure(text=self.basket[searchIndex]["Count"])

			#Increment Element
			elementIndex+=1

	def ChangeItemCount(self, itemIndex:str, delta:int):
		newCount = self.basket[itemIndex]["Count"] + delta #Calculate count after change
		
		#If new count will be zero, delete the item
		if newCount == 0:
			self.basket.pop(itemIndex)
		#Otherwise, apply the change
		stockCount = self.db.GetVariation(self.basket[itemIndex]["ProductID"])["stockLevel"]
		#Check the change won't make a negative stock
		if stockCount - delta < 0:
			messagebox.showwarning("Not Enough Stock", "Sorry, there is not enough stock to fulfil this request.")
		else:
			self.basket[itemIndex]["Count"] += delta
			self.ChangeStockLevel(itemIndex, delta)

		#Refresh display
		self.DisplayItems((self.currentPage-1) * 7)


	def ChangeStockLevel(self, itemIndex, delta):
		#Change stock level
		prodnum = self.basket[itemIndex]["ProductID"].split(":")[0]
		vari = self.db.GetVariation(self.basket[itemIndex]["ProductID"])
		item = self.db.GetItemByProductNumber(prodnum)
		vi = item["variations"].index(vari)
		item["variations"][vi]["stockLevel"] -= delta
		self.db.UpdateItem(prodnum, item)
		
