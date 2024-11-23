from app import App
from src.drivers.database.main import Database
from src.drivers.database.query import Query
from src.drivers.driver import getDriver
from src.models.book import Book

app = App()
app.run()

# query = Query("localhost", "3303", "root", "", "dane")
#
# data = {
#     "amount": 1,
#     "table": "books",
#     "filters":
#         {"id": 1}
# }
#
# query.makeQuery("select", data)
# print(query.execute())

dbdriver = getDriver('database')
db: Database = dbdriver.Database()
data = (db.get('isbn', 2137, Book))




