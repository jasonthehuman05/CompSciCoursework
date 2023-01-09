#This is the startfile
import StockDatabase

db = StockDatabase.StockDatabase()
print(db.database["items"][0]["productName"])