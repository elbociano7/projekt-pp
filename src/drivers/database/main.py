from src.drivers.database.worker import DBWorker
from src.drivers.driver import Driver


class Database(Driver):
  def get(self, modelClass, filters, limit = 1):
    return DBWorker.prepareSelect(modelClass, filters, limit)

  def insert(self, object):
    return DBWorker.prepareInsert(object).executeCommit()

  def update(self, object):
    DBWorker.prepareUpdate(object).executeCommit()

  def search(self, filters, model: object):
    pass