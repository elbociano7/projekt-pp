from src.drivers.database.main import Database
from src.drivers.driver import Driver, getDriver
from src.configuration import Config


class Model:
    serializable = ['id']
    table: str = ""
    id: int = None
    readonly: bool = False
    driver: Driver = getDriver(Config().get("DATABASE_DRIVER")).Database()

    def getByField(self, field: str, value: any, driver: Driver = None):
        if driver is None:
            driver = self.driver
        data = driver.get(self.__class__, {field: value})
        print(data)
        if data is not None:
            self.paramsToObject(data)

    def get(self, id: int = None):
        if id is None:
            id = self.id
        return self.getByField("id", id)

    def getVars(self):
        return self.serializable

    def save(self):
        if self.id is None:
            self.id = self.driver.insert(self).getLastRowId()
        else:
            self.driver.update(self)
        self.load()

    def paramsToObject(self, params):
        print('params', params)
        for param in params:
            self.__setattr__(param, params[param])

    def isConnected(self):
        return self.id is not None

    def load(self):
        if self.isConnected():
            self.get(self.id)

    @staticmethod
    def getMany(cls, key, value):
        drv: Driver = getDriver(Config().get("DATABASE_DRIVER")).Database()
        data = drv.get(cls, {key:value}, limit=None)
        objects = []
        if isinstance(data, list):
            for object in data:
                obj = cls()
                obj.paramsToObject(object)
                objects.append(obj)
        else:
            obj = cls()
            obj.paramsToObject(data)
            objects.append(obj)
        return objects

    @classmethod
    def getTableName(cls):
        return str.lower(cls.__name__) + "s"

    # RELATIONS

    def hasOne(self, object):
        field_name = str.lower(object.__name__) + "_id"
        object_id = getattr(self, field_name)
        return object().get(object_id)

    def belongsToMany(self, object):
        row_name = str.lower(self.__class__.__name__) + "_id"
        return object.getMany(object, row_name, self.id)

    @staticmethod
    def filterCollectionBy(collection: table, filters):
        return_collection = []
        for item in collection:
            filters_fullfill = True
            for filter in filters.keys():
                if getattr(item, filter) != filters[filter]:
                    filters_fullfill = False
            if filters_fullfill:
                return_collection.append(item)
        return return_collection




