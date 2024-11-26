from operator import itemgetter

from src.drivers.driver import getDriver
from src.models.model import Model
from src.configuration import Config, CONFIG


class Book(Model):
  """Book model
  """

  serializable = ['id', 'author', 'title', 'year', 'image', 'isbn']

  readonly = True

  def get(self, value: any, key: str = "id"):
    self.getByField(key, value)
    if self.isConnected() is False:
      apiDriver = getDriver(CONFIG.get("API_DRIVER")).Api()
      self.getByField(key, value, apiDriver)

  def loans(self):
    from src.models.loan import Loan
    return self.belongsToMany(Loan)

  def isAvailable(self):
    count = self.itemcount
    loans = Model.filterCollectionBy(self.loans(), {'returned': False})
    if len(loans) >= count:
      raise BookException('Brak dostepnych ksiazek!')
    else:
      return True

class BookException(Exception):
  pass

  


