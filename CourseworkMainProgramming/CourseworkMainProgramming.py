import StockDatabase, CustomerDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

db = StockDatabase.StockDatabase()

customerdb = CustomerDatabase.CustomerDB()
print(customerdb.database[0])

#mm = MainMenu.MainMenu(db)
