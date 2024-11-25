from inspect import Parameter

from mysql import connector

from pypika import Query, Table, Field, FormatParameter, MySQLQuery

from src.configuration import Config
from src.drivers.driver import DriverException

class QueryBuilder:
    query = None
    params = []

    def __init__(self, server, port, username, password, database):
        self.query = None
        try:
            self.connection = connector.connect(host=server, port=port, user=username, password=password, database=database)
            self.cursor = self.connection.cursor()
        except connector.Error as err:
            raise DriverException(err)

    def execute(self):
        if self.query is None:
            return False
        self.cursor.execute(self.query, self.params)
        return self

    def executeCommit(self):
        self.execute()
        self.connection.commit()
        return self

    def getLastRowId(self):
        return self.cursor.lastrowid

    def fetch(self):
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
        self.params = []
        table = Table(table)
        query = MySQLQuery.from_(table).select('*')
        if(operator == '='):
            if filters is not None:
                for filter in filters.keys():
                    query = query.where(table.field(filter) == FormatParameter())
                    self.params.append(filters[filter])
        elif(operator == 'LIKE'):
            pass
        if(limit is not None):
            query = query.limit(limit)
        self.query = query.offset(offset).get_sql()
        return self

    def makeInsertQuery(self, table, data):
        self.params = []
        table = Table(table)
        query = MySQLQuery.into(table).columns(*data.keys()).insert(*[FormatParameter() for _ in range(len(data.keys()))])
        self.params = list(data.values())
        self.query = query.get_sql()
        return self

    def makeUpdateQuery(self, table, data):
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
        data = {}
        for i in range(len(keys)):
            data[keys[i][0]] = values[0][i]
        return data


