import tkinter
import StockDatabase

class DetailsViewer:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase, itemNumber:str):
        self.item = db.GetItemByProductNumber(itemNumber)
        
        #Main Window
        self.root = tkinter.Tk()
        self.root.title(itemNumber)
        self.DrawWidgets()

        #Calculate size to accomodate all variations
        winSize = 100 + len(self.item['variations'])*25
        print(winSize)
        self.root.geometry(f"400x{winSize}")

        self.root.mainloop()
        
    def DrawWidgets(self):
        #Save Button
        saveButton = tkinter.Button(self.root, text="SAVE", command=lambda: self.Passer())
        saveButton.place(x=0,y=0,width=100,height=25)

        #Item Name
        itemNameEntry = tkinter.Entry(self.root)
        itemNameLabel = tkinter.Label(self.root, text="Item Name")
        itemNameEntry.insert(0, self.item["productName"])
        itemNameEntry.place(x=75, y=25, width=300)
        itemNameLabel.place(x=0, y=25)

        #Tags
        itemTagEntry = tkinter.Entry(self.root)
        itemTagLabel = tkinter.Label(self.root, text="Item Tags")

        tags = ""
        for tag in self.item["productTags"]:
            tags += f"{tag}, "
        tags = tags[:-2] #removes ", " from tag string

        itemTagEntry.insert(0, tags)
        itemTagEntry.place(x=75, y=50, width=300)
        itemTagLabel.place(x=0, y=50)

        #Variations
        itemVariationsHeaderLabel = tkinter.Label(self.root, text="Item Variations")
        itemVariationsHeaderLabel.place(x=0, y=75)
        self.DrawVariations()

    def DrawVariations(self):
        #Make header labels
        variationIDLabel = tkinter.Label(self.root, text="ID")
        variationIDLabel.place(x=0, y=100)
        variationNameLabel = tkinter.Label(self.root, text="Name")
        variationNameLabel.place(x=50, y=100)
        variationCostLabel = tkinter.Label(self.root, text="Cost")
        variationCostLabel.place(x=300, y=100)
        variationStockLabel = tkinter.Label(self.root, text="Stock")
        variationStockLabel.place(x=350, y=100)
        
        #Get Variations
        variations = self.item["variations"]
        
        yPos = 125 #start at y=125, since there are other labels to accomodate above
        for variation in variations:
            #For each variation, display the information
            variationIDEntry = tkinter.Entry(self.root)
            variationIDEntry.insert(0, variation["variationID"])
            variationIDEntry.place(x=0, y=yPos, width = 45)
            
            variationNameEntry = tkinter.Entry(self.root)
            variationNameEntry.insert(0, variation["variationName"])
            variationNameEntry.place(x=50, y=yPos, width = 245)
            
            variationCostEntry = tkinter.Entry(self.root)
            variationCostEntry.insert(0, variation["variationCost"])
            variationCostEntry.place(x=300, y=yPos, width = 45)
            
            variationStockEntry = tkinter.Entry(self.root)
            variationStockEntry.insert(0, variation["stockLevel"])
            variationStockEntry.place(x=350, y=yPos, width = 45)
            yPos+=25

    def Passer(self):
        pass