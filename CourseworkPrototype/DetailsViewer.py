import StockDatabase

class DetailsViewer:
    item = dict()
    
    def __init__(self, db:StockDatabase.StockDatabase, itemNumber:str):
        self.item = db.GetItemByProductNumber(itemNumber)
        
