import StockDatabase, CustomerDatabase, StaffDatabase, BasketDatabase
import MainCustomerScreen, CustomerLoginWindow
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

#Create Database Instances
db = StockDatabase.StockDatabase()
customerdb = CustomerDatabase.CustomerDB()
staffdb = StaffDatabase.StaffDB()
bdb = BasketDatabase.BasketDatabase()

bdb.AddToBasket("000001", "000001:1")

cl = CustomerLoginWindow.CustomerLoginWindow(db,customerdb)