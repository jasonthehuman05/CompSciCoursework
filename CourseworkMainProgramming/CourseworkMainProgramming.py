import StockDatabase, CustomerDatabase
import MainMenu
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

db = StockDatabase.StockDatabase()

customerdb = CustomerDatabase.CustomerDB()
print(customerdb.LoginCustomer(""))
#mm = MainMenu.MainMenu(db)
