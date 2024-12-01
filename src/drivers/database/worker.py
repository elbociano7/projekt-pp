from src.configuration import CONFIG
from src.drivers.database.querybuilder import QueryBuilder
from src.ui.ui import Window


class DBWorker:
  """
  Managing database queries and data preparation.
  """
  def getRows(self, table, filters, limit = 1):
    query = QueryBuilder.fromConfig()
    query.makeQuery("select", table, filters, limit)
    return query.execute()

  @staticmethod
  def checkDatabase():
    """
    Checks if database exists and has tables
    :return:
    """
    tables = ['readers', 'books', 'loans']
    db = CONFIG.get('DATABASE_NAME')
    query = QueryBuilder.fromConfig()
    fail = False
    for table in tables:
      try:
        if not query.checkDb(table, db):
          fail = True
          break
      except Exception as e:
        Window.makeErrorMessageBox('error', str(e))

    if fail:
      print("Database check failed. Setting up a new configuration")
      query.setupDb()


  @staticmethod
  def prepareInsert(object):
    """
    Prepare an insert query for the given object by extracting its properties and
    values to form appropriate data for insertion.

    :param object: The object for which the insert query needs to be prepared.
    :type object: Any class instance with `getVars` and `getTableName` methods.
    :return: A query object prepared for insertion with the data from the given object.
    :rtype: QueryBuilder
    """
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
    """
    Prepares an update query based on the given object.

    This method converts the object to a table data format and creates an
    update query using the QueryBuilder, configured through fromConfig.
    The resulting query is then returned.

    :param object: The object to be updated.
    :type object: SomeObjectType
    :return: An update query for the given object.
    :rtype: Query
    """
    data = DBWorker.objectToTable(object)
    query = QueryBuilder.fromConfig()
    query.makeUpdateQuery(object.getTableName(), data)
    return query

  @staticmethod
  def prepareSelect(modelClass, filters, limit = 1, offset = 0, operator = '='):
    """
    Prepare and execute a SELECT query with the given parameters, returning the
    fetched results.

    :param modelClass: The model class to query, from which the table name is derived.
    :type modelClass: Type
    :param filters: A dictionary of field-value pairs to use as the query filters.
    :type filters: dict
    :param limit: The maximum number of results to return. Defaults to 1.
    :type limit: int
    :param offset: The number of records to skip before starting to return results.
        Defaults to 0.
    :type offset: int
    :param operator: The comparison operator to use in the filters. Defaults to '='.
    :type operator: str
    :return: The result fetched from executing the query.
    :rtype: Any
    """
    query = QueryBuilder.fromConfig()
    q = query.makeSelectQuery(modelClass.getTableName(), filters, limit, offset, operator)
    result = q.execute().fetch()
    return result

  @staticmethod
  def objectToTable(object):
    """
    Converts an object's attributes to a dictionary.

    This method takes an object and converts its attributes into a dictionary where
    keys are the names of the attributes, and values are their corresponding values.

    :param object: The object whose attributes are to be converted into a dictionary.
    :type object: Any
    :return: A dictionary with the object's attributes and their corresponding values.
    :rtype: dict
    """
    data = {}
    for prop in object.getVars():
      if hasattr(object, prop):
        data[prop] = getattr(object, prop)
      else:
        data[prop] = ''
    return data