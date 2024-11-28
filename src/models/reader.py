from datetime import datetime

from src.models.book import Book, BookException
from src.models.model import Model

class Reader(Model):

  serializable = ['id', 'firstname', 'lastname']

  def loans(self):
    """
    Loans relation
    :return:
    """
    from src.models.loan import Loan
    return self.belongsToMany(Loan)

  def loanBook(self, book, end_time: datetime):
    """
    Method for loaning a book. It creates a relationship object between the reader and the book
    with data given in function arguments.
    :param book: Book to make relation with
    :param end_time: Loan end time
    :return:
    """
    from src.models.loan import Loan
    if book.isAvailable():
      print(book.id, self.id)
      loan = Loan()
      loan.reader_id = self.id
      loan.book_id = book.id
      loan.start_date = datetime.now()
      loan.end_date = end_time
      loan.returned = False
      loan.save()
    else:
      raise BookException('Book not available')


  