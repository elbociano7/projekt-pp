from app import App
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


reader = Reader()

reader.get(1)
if(reader.isConnected()):
    loans = reader.loans()
    for loan in loans:
        print(bool(loan.returned))





