#This is the startfile
import StockDatabase

db = StockDatabase.StockDatabase()
item = db.GetItemByProductNumber("000001")
print(item["productName"])
variation = db.GetVariation("000001:1")
print(variation["variationName"])
#print(db.database["items"][0]["productName"])
#db.WriteDatabase()