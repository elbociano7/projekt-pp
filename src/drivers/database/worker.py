from src.drivers.database.query import Query


class DBWorker:

  def getRows(self, table, filters, limit = 1):
    query = Query.fromConfig()
    query.makeQuery("select", table, filters, limit)
    return query.execute()

  def makeObject(self, object_type, params):
    pass