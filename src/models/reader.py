from datetime import datetime

from src.models.book import Book
from src.models.model import Model

class Reader(Model):

  serializable = ['id', 'firstname', 'lastname']

  def loans(self):
    from src.models.loan import Loan
    return self.belongsToMany(Loan)

  def loanBook(self, book: Book, endTime: datetime):
    from src.models.loan import Loan
    if book.isAvailable():
      loan = Loan()
      loan.reader_id = self.id
      loan.book_id = book.id
      loan.start_date = datetime.now()
      loan.end_date = endTime
      loan.returned = False
      loan.save()


  