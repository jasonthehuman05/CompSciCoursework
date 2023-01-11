#This is the startfile
import StockDatabase

db = StockDatabase.StockDatabase()
db.SearchForItem("20 masonry nails")
#print(db.database["items"][0]["productName"])