from __future__ import annotations#To fix circular import issue
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
        self.DrawVariants()

    def DrawVariants(self):
        variants = self.item["variations"]

        font = "default 32 normal"
        height = 64
        padding = 8
        startAt = 18
        self.variantContainers = []
        for i in range(0, len(variants)):
            #get details -> calculate widget locations -> draw UI into arrays -> display
            yPos = startAt + (padding+height)*i
            self.variantContainers.append(tkinter.Frame(self.variantFrame))
            self.variantContainers[i].place(x=8,y=yPos,width=1888,height=height)
            variantNumber = tkinter.Label(self.variantContainers[i], text = f"Variation ID: {variants[i]['variationID']}",anchor="w").place(x=8,y=48, height = 16, width=1000)
            variantName = tkinter.Label(self.variantContainers[i], text = variants[i]["variationName"],anchor="w",font=font).place(x=8,y=0, height = 48, width = 1000)
            
            #This all makes a string that holds the price. There were some character set issues between ISO 8859-1 and UTF-8. this is how i fixed it.
            pound = bytes.fromhex('c2a3').decode('utf-8')
            cost = ("{0:.2f}").format(variants[i]["variationCost"]) #formats price with the 2DP
            finalString = pound+cost

            variantCost = tkinter.Label(self.variantContainers[i], text = finalString, font=font).place(x=1278,y=8,width=200)
            variantStock = tkinter.Label(self.variantContainers[i], text = f'{variants[i]["stockLevel"]} in stock', font=font).place(x=1008,y=8, width=250)

            pNumWithVariation = f"{self.productNumber}:{variants[i]['variationID']}"
            addToBasketButton = tkinter.Button(self.variantContainers[i], text="ADD TO BASKET", bg=colorfile.accent[3], command= lambda x = pNumWithVariation: self.AddToBasket(pNumWithVariation))
            addToBasketButton.place(x=1500,y=8,height=height-16,width=380)
        
    def AddToBasket(self, pNumWithVariation): #TODO: ADD
        pass



