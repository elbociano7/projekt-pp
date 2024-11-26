import datetime

from app import App
from src.models.book import Book
from src.models.reader import Reader

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
# print(query.execute()


book = Book()

book.get(1)

reader = Reader()
reader.get(2)
reader.loanBook(book, datetime.datetime.now() + datetime.timedelta(days=30))
print(reader.loans())

print('is available: ', book.isAvailable())





