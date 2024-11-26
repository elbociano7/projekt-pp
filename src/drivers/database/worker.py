from src.configuration import CONFIG
from src.drivers.database.querybuilder import QueryBuilder


class DBWorker:

  def getRows(self, table, filters, limit = 1):
    query = QueryBuilder.fromConfig()
    query.makeQuery("select", table, filters, limit)
    return query.execute()

  @staticmethod
  def prepareInsert(object):
    data = {}
    for prop in object.getVars():
      if(hasattr(object, prop)):
        data[prop] = getattr(object, prop)
      else:
        data[prop] = None
    query = QueryBuilder.fromConfig()
    query.makeInsertQuery(object.getTableName(), data)
    return query

  @staticmethod
  def prepareUpdate(object):
    data = DBWorker.objectToTable(object)
    query = QueryBuilder.fromConfig()
    query.makeUpdateQuery(object.getTableName(), data)
    return query

  @staticmethod
  def prepareSelect(modelClass, filters, limit = 1, offset = 0, operator = '='):
    query = QueryBuilder.fromConfig()
    result = query.makeSelectQuery(modelClass.getTableName(), filters, limit, offset, operator).execute().fetch()
    return result

  @staticmethod
  def objectToTable(object):
    data = {}
    for prop in object.getVars():
      data[prop] = getattr(object, prop)
    return data