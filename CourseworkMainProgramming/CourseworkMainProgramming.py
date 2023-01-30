import StockDatabase, CustomerDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

db = StockDatabase.StockDatabase()

customerdb = CustomerDatabase.CustomerDB()
print(customerdb.GetCustomer("000001"))
#mm = MainMenu.MainMenu(db)
