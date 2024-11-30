import os
from inspect import Parameter

from mysql import connector
from pypika import Query, Table, Field, FormatParameter, MySQLQuery, Criterion, functions

from src.configuration import Config, CONFIG
from src.drivers.driver import DriverException

class QueryBuilder:
    """
    Handles building and executing SQL queries for database operations.

    The QueryBuilder class provides methods for constructing and executing SQL queries such
    as SELECT, INSERT, and UPDATE with parameterized values. It manages database connections
    and query execution, ensuring safe and efficient interactions with the database.

    :ivar query : Stores the constructed SQL query.
    :type query: str | None
    :ivar params: Stores the parameters for the SQL query.
    :type params: list
    """
    query = None
    params = []

    def __init__(self, server, port, username, password, database):
        """
        Class constructor. Creates a new QueryBuilder instance with the specified connection settings and credentials.

        :param str server: The hostname or IP address of the database server
        :param int port: The port number of the database server
        :param str username: The username for database authentication
        :param str password: The password for database authentication
        :param str database: The name of the database to connect to
        """
        self.query = None
        try:
            self.connection = connector.connect(host=server, port=port, user=username, password=password, database=database)
            self.cursor = self.connection.cursor(buffered=False)
        except connector.Error as err:
            raise DriverException(err)

    def execute(self):
        """
        Executes prepared query.
        """
        if self.query is None:
            return False
        self.cursor.execute(self.query, self.params)
        return self

    def executeCommit(self):
        """
        Manages database transactions and provides methods to execute and commit
        SQL commands.
        """
        self.execute()
        self.connection.commit()
        return self

    def getLastRowId(self):
        """
        Get last inserted row id

        :return: The ID of the last inserted row.
        :rtype: int
        """
        return self.cursor.lastrowid

    def fetch(self):
        """
        Fetches all rows from the cursor and returns them in a structured format.
        This method retrieves every row from the database cursor. If no rows are
        retrieved, it returns None. If multiple rows are retrieved, it returns a list
        of dictionaries where each dictionary represents a row. If only one row is
        retrieved, it returns a single dictionary representing that row.

        :return: None if no rows are found, a dictionary if one row is found,
                 or a list of dictionaries if multiple rows are found.
        :rtype: None | dict | list[dict]
        """
        values = self.cursor.fetchall()
        keys = self.cursor.description
        if self.cursor.rowcount == 0:
            return None
        if self.cursor.rowcount > 1:
            data = []
            for value in values:
                data.append(QueryBuilder.toDict(keys, [value]))
            return data
        return QueryBuilder.toDict(keys, values)

    def makeSelectQuery(self, table, filters = None, limit = 50, offset = 0, operator = '='):
        """
        Constructs a SQL SELECT query with the specified table, filters, limit, offset, and operator. The operator parameter
        specifies the condition operator ('=' or 'LIKE'). The method also adds the pagination functionality
        with the limit and offset parameters.

        :param str table: The name of the table to query
        :param dict filters: Optional; A dictionary of columns and their corresponding values to filter the results
        :param int limit: Optional; The maximum number of records to return. Defaults to 50
        :param int offset: Optional; The number of records to skip from the beginning. Defaults to 0
        :param str operator: Optional; The condition operator for filters. Can be either '=' or 'LIKE'. Defaults to '='
        :return: The instance of the class with the constructed query
        :rtype: self
        """
        self.params = []
        table = Table(table)
        query = MySQLQuery.from_(table).select('*')
        if filters is not None:
            if operator == '=':
                for filter in filters.keys():
                    query = query.where(table.field(filter) == FormatParameter())
                    self.params.append(filters[filter])
            elif operator == 'LIKE':
                criterions = []
                fields = []
                val: str = ''
                for filter in filters.keys():
                    fields.append(functions.Upper(table.field(filter)))
                    val = filters[filter]
                filt = str.upper("%" + self.connection.converter.escape(val.replace(' ', '%')) + "%")
                query = query.where(functions.Concat(*fields).like(filt))
        if limit is not None:
            query = query.limit(limit)

        self.query = query.offset(offset).get_sql()
        return self

    def makeInsertQuery(self, table, data):
        """
        Constructs a SQL Insert query with the provided table and data.

        :param str table: The name of the table where data should be inserted
        :param dict data: A dictionary containing column names and their corresponding values
        :return: An instance of the current object with the constructed query
        """
        self.params = []
        table = Table(table)
        query = MySQLQuery.into(table).columns(*data.keys()).insert(*[FormatParameter() for _ in range(len(data.keys()))])
        self.params = list(data.values())
        self.query = query.get_sql()
        return self

    def makeUpdateQuery(self, table, data):
        """
        Constructs a SQL UPDATE query with the provided table and data.
        Update is executed on a row with `id` field equal to `data['id']`

        :param str table: The name of the table where data should be updated
        :param dict data: A dictionary containing column names and their corresponding values with object id.
        :return: An instance of the current object with the constructed query
        """
        self.params = []
        id :int = data['id']
        table = Table(table)
        query = MySQLQuery.update(table).where(table.id == id)
        for field in data.keys():
            query = query.set(table.field(field), FormatParameter())
            self.params.append(data[field])
        self.query = query.get_sql()
        return self

    @staticmethod
    def fromConfig():
        """
        Create a QueryBuilder instance using configuration settings.

        This method initializes a QueryBuilder instance by using the configuration
        settings obtained from a Config object. The specific settings used are
        'DATABASE_HOST', 'DATABASE_PORT', 'DATABASE_USER', 'DATABASE_PASSWORD',
        and 'DATABASE_NAME'.

        :return: A QueryBuilder instance configured with settings from Config.
        :rtype: QueryBuilder
        """
        config = Config()
        query = QueryBuilder(
            config.get('DATABASE_HOST'),
            config.get('DATABASE_PORT'),
            config.get('DATABASE_USER'),
            config.get('DATABASE_PASSWORD'),
            config.get('DATABASE_NAME')
        )
        return query

    @staticmethod
    def toDict(keys, values):
        """
        Converts lists of keys and values into a dictionary.

        Given a list of keys and a list of values, this method creates a dictionary
        where each key from the keys list is associated with the corresponding element
        at the same index in the values list.

        :param list[str] keys: List of keys for the dictionary
        :param list[list] values: Nested list of values for the dictionary
        :return: Dictionary created by combining keys and values
        :rtype: dict
        """
        data = {}
        for i in range(len(keys)):
            data[keys[i][0]] = values[0][i]
        return data

    @staticmethod
    def getDebugCursor():
        connection = connector.connect(
            host=CONFIG.get('DATABASE_HOST'),
            port=CONFIG.get('DATABASE_PORT'),
            user=CONFIG.get('DATABASE_USER'),
            password=CONFIG.get('DATABASE_PASSWORD'),
            database=CONFIG.get('DATABASE_NAME'))
        cursor = connection.cursor(buffered=True)
        return (connection, cursor)

    def checkDb(self, table):
        (conn, cursor) = self.getDebugCursor()
        query = f"SELECT * FROM information_schema.`TABLES` WHERE `TABLE_NAME` = '{table}'"
        cursor.execute(query)
        if cursor.rowcount == 0:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

    def setupDb(self):
        (conn, cursor) = self.getDebugCursor()
        lines = []
        with open(os.path.dirname(os.path.realpath(__file__))+"/schema.sql") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            cursor.execute(line)
        #cursor.execute(f.read(), multi=True)
        #cursor.close()
        #conn.close()



