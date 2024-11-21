from model import Model
from reader import Reader
from book import Book

class Loan(Model):

  start_date: str = ""
  end_date: str = ""
  returned: bool = False

  def reader(self):
    return self.hasOne(Reader.__class__)
  
  def book(self):
    return self.hasOne(Book.__class__)

