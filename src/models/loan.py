from src.models.model import Model

class Loan(Model):

  serializable = ['id', 'reader_id', 'book_id', 'start_date', 'end_date', 'returned']

  def reader(self):
    from src.models.reader import Reader
    print(Reader)
    return self.hasOne(Reader)
  
  def book(self):
    from src.models.book import Book
    return self.hasOne(Book)

