#This is the startfile
import StockDatabase

db = StockDatabase.StockDatabase()

#Working test
itemToChange = db.GetItemByProductNumber("000001")
itemToChange["productName"] = "3mm Timber Nails: 25 Count"

db.UpdateItem("000001", itemToChange)

print(db.database)

#Shouldn't work
itemToChange = db.GetItemByProductNumber("000001")
itemToChange["productName"] = "3mm Timber Nails: 25 Count"

db.UpdateItem("123456", itemToChange)