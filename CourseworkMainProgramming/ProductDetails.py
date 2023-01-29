from __future__ import annotations #To fix circular import issue
import tkinter
import colorfile
import StockDatabase
import MainMenu

class ProductDetails:
    def __init__(self, db:StockDatabase.StockDatabase, mainScreen:MainMenu.MainMenu, productNumber:str):
        #Public variables
        self.db = db
        self.mainScreen = mainScreen
        self.productNumber = productNumber

        #Find item
        self.item = self.db.GetItemByProductNumber(self.productNumber)

        #Create Window
        self.root = tkinter.Toplevel()
        self.root.title(f"Product Details: {productNumber}")
        self.root.geometry("1920x1080")
        self.root.attributes('-fullscreen', True) #Makes the window appear in fullscreen mode.
        self.DrawWidgets()
        self.root.mainloop()

    def DrawWidgets(self):
        #Top Bar Frame
        self.topBarFrame = tkinter.Frame(self.root, bg=colorfile.topbarcolor)
        self.topBarFrame.place(x=0,y=0,width=1920,height=64)
        
        #back button
        self.returnButton = tkinter.Button(self.topBarFrame, text="BACK", command=lambda:self.root.destroy())
        self.returnButton.place(x=8,y=8,width=128,height=48)

        #Main Body Frame
        self.mainBodyFrame = tkinter.Frame(self.root, bg=colorfile.accent[0])
        self.mainBodyFrame.place(x=0,y=64,width=1920,height=1016)
        
        #Product Details
        self.productNameLabel = tkinter.Label(self.mainBodyFrame, text=self.item["productName"], font = "default 72 normal", bg=colorfile.accent[0])
        self.productNameLabel.place(x=8,y=4,height=88)
        self.productNumberLabel = tkinter.Label(self.mainBodyFrame, text=self.item["productNumber"], font = "default 26 normal", bg=colorfile.accent[0])
        self.productNumberLabel.place(x=8,y=92,height=28)

        #Variants Frame
        self.variantFrame = tkinter.Frame(self.mainBodyFrame, bg=colorfile.accent[1])
        self.variantFrame.place(x=8,y=134,width=1904,height=938)

    def DrawVariants(self):
        pass



