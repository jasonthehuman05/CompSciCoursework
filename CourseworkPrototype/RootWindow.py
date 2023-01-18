import tkinter
import StockDatabase
import math
import DetailsViewer
import ItemCreator

class RootWindow:
    root = None
    pageNumber = 1
    pageCount = 1

    db = None
    itemNameLabel = []
    itemNumberLabel = []
    itemOpenButton = []

    def __init__(self, db:StockDatabase.StockDatabase):
        self.db = db
        self.root = tkinter.Tk()
        self.root.title("BuildrightDB Prototype: Inventory Manager")
        self.DrawWidgets()
        self.root.geometry("600x400")
        self.root.mainloop()
        
    def DrawWidgets(self):
        #CreateButton
        self.createButton = tkinter.Button(self.root, text="ADD INVENTORY", command= lambda:self.AddInventory())
        self.createButton.pack()
        self.createButton.place(x=8, y=8, height=32, width=100, anchor="nw")

        #InventoryFrame
        #Since TKinter's scrollbar doesn't seem to work well, I am making a different
        #method of scrolling the page
        self.inventoryFrame = tkinter.Frame(self.root)
        self.inventoryFrame.configure(background='#aaaaaa')
        self.inventoryFrame.pack()
        self.inventoryFrame.place(x=8, y=48, width = 584, height=312, anchor="nw")

        self.GenerateItemInformationHolders()
        self.LoadPage()

        self.pageLabel = tkinter.Label(self.root, text=f"Page {self.pageNumber} of {self.pageCount}")
        self.pageLabel.place(x=300, y=372, anchor="center")
        
        self.prevPageButton = tkinter.Button(self.root, text="<=", command=lambda:self.ChangePage(-1))
        self.prevPageButton.place(x=8, y=360)

        self.nextPageButton = tkinter.Button(self.root, text="=>", command=lambda:self.ChangePage(1))
        self.nextPageButton.place(x=565, y=360)

    def GenerateItemInformationHolders(self):
        #Generates the holders for the item information in the inventory frame

        #values to use for positioning
        marginBetweenRows = 8

        for i in range(0, 12):
            #Generate Row Y position
            rowYPosition = ((18+marginBetweenRows)*i)+2

            #generate buttons
            self.itemOpenButton.append(tkinter.Button(self.inventoryFrame, text="View Details", command=self.Passer()))
            self.itemOpenButton[i].place(x=8, y=rowYPosition, height=18, width=100)

            #generate prod num labels
            self.itemNumberLabel.append(tkinter.Label(self.inventoryFrame, text="000000"))
            self.itemNumberLabel[i].place(x=116, y=rowYPosition, height=18, width=48)

            #generate item informaiton labels
            self.itemNameLabel.append(tkinter.Label(self.inventoryFrame, text="000000"))
            self.itemNameLabel[i].place(x=172, y=rowYPosition, height=18, width=400)
        
        #While its not part of the item information holder, calculate the number of pages
        itemcount = len(self.db.database["items"])
        self.pageCount = math.ceil(itemcount / 12)

    def EmptyItemInformation(self): #reset the information in the holders
        for i in range(0, 12):
            self.itemOpenButton[i].config(command=lambda: self.Passer())
            self.itemNumberLabel[i].config(text="000000")
            self.itemNameLabel[i].config(text="NO ITEM")

    def ChangePage(self, direction:int):
        #Define new page number
        tPageNum = self.pageNumber + direction
        if tPageNum > 0 and tPageNum <= self.pageCount:
            self.pageNumber += direction
            self.pageLabel.configure(text=f"Page {self.pageNumber} of {self.pageCount}")
            self.LoadPage()

    def LoadPage(self):
        #Empty the page
        self.EmptyItemInformation()
        #Get the start and end indexes
        startPoint = (self.pageNumber-1)*12
        endPoint = startPoint+11

        if endPoint > len(self.db.database["items"]):
            endPoint = len(self.db.database["items"])-1

        elementNumber = 0
        for i in range(startPoint, endPoint+1):
            itemMain = self.db.database["items"][i]
            self.itemOpenButton[elementNumber].config(command=lambda lambdaItem=itemMain: DetailsViewer.DetailsViewer(self.db, lambdaItem["productNumber"]))
            self.itemNumberLabel[elementNumber].config(text=itemMain["productNumber"])
            self.itemNameLabel[elementNumber].config(text=itemMain["productName"])

            elementNumber += 1

    def AddInventory(self):
        ic = ItemCreator.ItemCreator(self.db)

    def Passer(self):
        pass