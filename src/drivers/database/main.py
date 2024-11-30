from src.drivers.database.worker import DBWorker
from src.drivers.driver import Driver


class Database(Driver):
  """
  This class interfaces with a database system through a set of methods
  to perform create, read, update, and search operations.
  """

  def checkDatabase(self):

    DBWorker.checkDatabase()



  def get(self, modelClass, filters, limit = 1):
    """
    Retrieves data from a database based on the given model class, filters, and limit.

    This function prepares and executes a SELECT query on the database using the
    specified model class and filters. The query result is limited to the specified
    number of records.

    :param modelClass: The database model class to query data from.
    :type modelClass: type
    :param filters: The filtering criteria for the query.
    :type filters: dict
    :param limit: The maximum number of records to retrieve.
    :type limit: int
    :return: The result of the prepared SELECT query.
    :rtype: any
    """
    data = DBWorker.prepareSelect(modelClass, filters, limit)
    return data

  def insert(self, object):
    """
    Insert an object into the database.

    This method prepares an insert query for the provided object and executes
    the query with a commit to the database.

    :param object: The object to be inserted into the database.
    :type object: Any
    :return: The result of the commit operation after executing the prepared
             insert query.
    :rtype: Any
    """
    query = DBWorker.prepareInsert(object).executeCommit()
    return query.getLastRowId()

  def update(self, object):
    """
    Method responsible for updating an object in the database.

    :param object: The object to be updated in the database.
    :type object: Any

    :rtype: Void
    """
    DBWorker.prepareUpdate(object).executeCommit()

  def search(self, modelClass, filters):
    """
    Executes a search query on the database for the given model class and filters.

    This method utilizes the DBWorker's prepareSelect method to search for records
    based on the specified filters, limiting results to 50 entries and using the
    'LIKE' operator for pattern matching.

    :param modelClass: The class model representing the database table to search.
    :type modelClass: type
    :param filters: A dictionary containing field-value pairs to filter the search results.
    :type filters: dict
    :return: A prepared SQL select query for the given filters.
    :rtype: str
    """
    return DBWorker.prepareSelect(modelClass, filters, limit=50, operator='LIKE')