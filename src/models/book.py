from model import Model
from ..configuration import Config

class Book(Model):
  """Book model
  """

  readonly = True
  driver = "google"

  name: str = ""
  isbn: str = ""
  author: str = ""
  year: int = None

  def get(self, value: any, field: str = "id"):
    data = self.getByField(field, value, self.driver)
    if(data == None):
      return self.getByField(field, value, Config.get("DATABASE_DRIVER"))
    
  


