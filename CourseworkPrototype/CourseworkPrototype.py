#This is the startfile
import StockDatabase

db = StockDatabase.StockDatabase()

#Add Item Test
variation1 = {
	"variationID": "1",
	"variationName": "Ocean Sky",
	"variationCost": 16.30,
	"stockLevel": 59
}

tags = ["paint", "indoor", "walls", "matt", "silk", "home"]

db.CreateItem("5L Matte Paint", tags, [variation1])

print(db.database)