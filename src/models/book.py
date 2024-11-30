from src.drivers.driver import getDriver
from src.models.model import Model
from src.configuration import Config, CONFIG


class Book(Model):
  """Book model
  """

  serializable = ['id', 'author', 'title', 'year', 'image', 'isbn', 'itemcount']

  readonly = True

  def loans(self):
    """
    Loans relation
    :return:
    """
    from src.models.loan import Loan
    return self.belongsToMany(Loan)

  def isAvailable(self):
    """
    Determines the availability of an item based on its loan status.

    This method checks if the number of active (not returned)
    loans is less than the total item count. If the number of
    active loans equals or exceeds the item count, the item is
    considered unavailable.

    :return: A boolean value indicating whether the item is
             available (True) or not (False).
    :rtype: bool
    """
    count = self.itemcount
    loans = Model.filterCollectionBy(self.loans(), {'returned': False})
    if len(loans) >= count:
      return False
    else:
      return True

  @staticmethod
  def searchBySingleString(cls, fields, word):
    """
    Search for a single string across specified fields in a class.

    This method interfaces with an API driver to search for a single word within
    specified fields of a class. The results are processed, and instances of the
    `Book` class are created or updated accordingly. The method returns a list of
    book objects with the search results.

    :param cls: The class in which to search for the word.
    :type cls: type
    :param fields: The fields within the class to search.
    :type fields: list
    :param word: The word to search for within the specified fields.
    :type word: str
    :return: A list of `Book` objects containing the search results.
    :rtype: list of Book
    """

    def processBook(id, data):
      bookObject = Book()
      if not Book.entryExists(Book, id):
        bookObject.paramsToObject(data)
        bookObject.itemcount = CONFIG.get("DEFAULT_BOOK_COUNT")
        bookObject.save()
      else:
        bookObject.get(id)
      return bookObject

    apiDriver = getDriver(CONFIG.get("API_DRIVER")).Api()
    word = word.strip(' ')
    if word == '':
      raise BookSearchException("search_field_cannot_be_empty")
    if len(word) > 2 and word[0:3] == "id:":
      if len(word) == 3:
        raise BookSearchException("invalid_book_id")
      id = word[3::]
      data = apiDriver.get(cls, id)
      if data is not None:
        id = data['id']
        return [processBook(id, data)]
      return []
    data = apiDriver.searchSingleWord(cls, word)
    books = []
    for book in data:
      books.append(processBook(book['id'], book))
    return books



class BookSearchException(Exception):
  pass

  


