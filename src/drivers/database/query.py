from ftplib import print_line

from mysql import connector

from src.configuration import Config
from src.drivers.driver import DriverException

class Query:
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
        print(self.query)
        if self.query is None:
            return False
        self.cursor.execute(self.query, self.params)
        values = self.cursor.fetchall()
        keys = self.cursor.description
        return Query.toDict(keys, values)


    def makeQuery(self, queryType: str, table: str, filters = None, limit = None):
        if queryType == "select":
            use_where = filters != None
            query = f"SELECT * from {table} "
            if use_where:
                first = True
                for filter in filters.keys():
                    if not first:
                        query+= "AND "
                    first = False
                    query += f"WHERE {filter}=%s "
                    self.params.append(filters[filter])
            if limit != None:
                query += f"LIMIT {limit} "
            self.query = query
        elif queryType == "insert":
            pass
        elif queryType == "update":
            pass
        elif queryType == "delete":
            pass

    @staticmethod
    def fromConfig():
        config = Config()
        query = Query(
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

