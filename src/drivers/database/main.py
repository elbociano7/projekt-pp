from src.drivers.database.worker import DBWorker
from src.models.model import Model

class Database:
  def get(self, field: str, value: any, model: Model):
    results = DBWorker().getRows(model.getTableName(), {field: value})
    if results == []:
      return None
    return results

  def search(self, filters, model: object):
    pass