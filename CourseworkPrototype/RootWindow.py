import tkinter

class RootWindow:
    root = None
    pageNumber = 1
    pageCount = 18

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
        self.inventoryFrame.place(x=8, y=48, width = 584, height=300, anchor="nw")

        self.LoadPage()

        self.pageLabel = tkinter.Label(self.root, text=f"Page {self.pageNumber} of {self.pageCount}")
        self.pageLabel.place(x=300, y=360, anchor="center")
        
        self.prevPageButton = tkinter.Button(self.root, text="<=", command=lambda:self.ChangePage(-1))
        self.prevPageButton.place(x=8, y=348)

        self.nextPageButton = tkinter.Button(self.root, text="=>", command=lambda:self.ChangePage(1))
        self.nextPageButton.place(x=565, y=348)

    def GenerateItemInformation(self):
        #Generates the holders for the item information
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