import tkinter

class RootWindow:
    root = None
    pageNumber = 1
    pageCount = 18

    itemNameLabel = []
    itemNumberLabel = []
    itemOpenButton = []

    def __init__(self):
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
        self.inventoryFrame.place(x=8, y=48, width = 584, height=306, anchor="nw")

        self.GenerateItemInformation()

        self.pageLabel = tkinter.Label(self.root, text=f"Page {self.pageNumber} of {self.pageCount}")
        self.pageLabel.place(x=300, y=366, anchor="center")
        
        self.prevPageButton = tkinter.Button(self.root, text="<=", command=lambda:self.ChangePage(-1))
        self.prevPageButton.place(x=8, y=354)

        self.nextPageButton = tkinter.Button(self.root, text="=>", command=lambda:self.ChangePage(1))
        self.nextPageButton.place(x=565, y=354)

    def GenerateItemInformation(self):
        #Generates the holders for the item information in the inventory frame

        #values to use for positioning
        marginBetweenRows = 8
        elementHeight = 8

        for i in range(0, 12):
            #Generate Row Y position
            rowYPosition = ((18+marginBetweenRows)*i)+2

            #generate buttons
            self.itemNameLabel.append(tkinter.Button(self.inventoryFrame, text="View Details", command=lambda: print("Unassigned!")))
            self.itemNameLabel[i].place(x=8, y=rowYPosition, height=18, width=100)
        pass

    def ChangePage(self, direction:int):
        #Define new page number
        tPageNum = self.pageNumber + direction
        if tPageNum > 0 and tPageNum <= self.pageCount:
            self.pageNumber += direction
            self.pageLabel.configure(text=f"Page {self.pageNumber} of {self.pageCount}")
            self.LoadPage()

    def LoadPage(self):
        pass

    def AddInventory(self):
        pass

n = RootWindow()