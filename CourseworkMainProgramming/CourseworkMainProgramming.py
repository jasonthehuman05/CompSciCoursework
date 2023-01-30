import StockDatabase, CustomerDatabase, StaffDatabase
import MainCustomerScreen
'''
╔═══════════════════════╗
║Application Entry Point║
╚═══════════════════════╝
'''

#Create Database Instances
db = StockDatabase.StockDatabase()
customerdb = CustomerDatabase.CustomerDB()
staffdb = StaffDatabase.StaffDB()

mm = MainCustomerScreen.MainCustomerScreen(db)
