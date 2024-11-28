from src.models.model import Model

class Loan(Model):

  serializable = ['id', 'reader_id', 'book_id', 'start_date', 'end_date', 'returned']

  def reader(self):
    """
    Reader relation
    :return:
    """
    from src.models.reader import Reader
    return self.hasOne(Reader)
  
  def book(self):
    """
    Book relation
    :return:
    """
    from src.models.book import Book
    return self.hasOne(Book)

