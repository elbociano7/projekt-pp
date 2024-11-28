from src.drivers.database.main import Database
from src.drivers.driver import Driver, getDriver
from src.configuration import Config


class Model:
    """
    The Model class serves as a base class for database models, providing methods
    for CRUD operations and serialization.

    This class enables interaction with the database through a defined driver,
    allowing models to be retrieved, saved, and manipulated. It also offers utilities
    to serialize models to dictionaries and to handle relationships between different models.

    :ivar serializable: List of attributes that will be serialized / send to database.
    :type serializable: list
    :ivar table: Name of the table associated with the model.
    :type table: str
    :ivar id: Unique identifier for the model instance.
    :type id: int
    :ivar readonly: Flag indicating whether the model is read-only.
    :type readonly: bool
    :ivar driver: Database driver used for database operations.
    :type driver: Driver
    """
    serializable = ['id']
    table: str = ""
    id: int = None
    readonly: bool = False
    connected: bool = False
    driver: Driver = getDriver(Config().get("DATABASE_DRIVER")).Database()

    def getByField(self, field: str, value: any, driver: Driver = None):
        """
        Retrieve an object from the data source based on the field and value
        specified. If no driver is provided, the method will use the instance's
        default driver.

        :param field: The field to query in the data source.
        :type field: str
        :param value: The value to match against the specified field.
        :type value: any
        :param driver: The driver to use for the data source query (optional).
        :type driver: Driver, optional
        :return: None
        """
        if driver is None:
            driver = self.driver
        data = driver.get(self.__class__, {field: value})
        if data is not None:
            self.connected = True
            self.paramsToObject(data)
        return self

    def get(self, id: int = None):
        """
        Retrieves an object based on its ID. If no ID is provided, it
        defaults to using the instance's ID.

        :param id: The unique identifier of the object to retrieve.
        :type id: int, optional
        :return: The object corresponding to the provided ID.
        :rtype: Any
        """
        if id is None:
            id = self.id
        return self.getByField("id", id)

    def getVars(self):
        """
        Retrieve serializable variables.
        """
        return self.serializable

    def save(self):
        """
        Saves the current state of the object to the database. If the object does not
        have an ID, it inserts the object into the database and sets the ID. If the
        object already §has an ID, it updates the existing record in the database.
        After saving, it reloads the object.

        :raises DatabaseError: If there is an issue with the database operation.

        :return: None
        """
        if self.id is None or self.connected is False:
            self.id = self.driver.insert(self).getLastRowId()
        else:
            self.driver.update(self)
        self.load()

    def paramsToObject(self, params):
        """
        Converts a dictionary of parameters into object attributes.

        This method takes a dictionary of parameters and sets them as
        attributes of the object. Each key in the dictionary becomes an
        attribute name, and the corresponding value becomes the attribute
        value.

        :param params: Dictionary of parameters to be converted into object
                       attributes.
        :type params: dict
        """
        for param in params:
            self.__setattr__(param, params[param])

    def isConnected(self):
        """
        The Connection class checks if the current instance is connected to a database object.

        It determines connectivity based on the presence of a valid
        identifier.
        """
        return self.id is not None and self.connected

    def load(self):
        """
        DataLoader is responsible for loading data from a source if connected.

        This class provides functionalities to check the connection status and
        load data based on the provided identifier.

        :ivar id: str: The identifier used for loading data.
        :ivar isConnected: Callable[[], bool]: Function to check if the source is connected.
        :ivar get: Callable[[str], None]: Function to retrieve data given an identifier.
        """
        if self.id is not None:
            self.get(self.id)
            self.connected = True

    def serialize(self):
        """
        Serializes the attributes specified in the `self.serializable` list to a dictionary.

        This method iterates over each attribute name listed in `self.serializable`.
        For each attribute name, it checks if the attribute exists in the instance.
        If the attribute exists, its value is added to the dictionary with the attribute
        name as the key. If the attribute does not exist, the key is set to `None` in the
        resulting dictionary.

        :return: A dictionary containing the serialized attributes.
        :rtype: dict
        """
        data = {}
        for key in self.serializable:
            if hasattr(self, key):
                data[key] = getattr(self, key)
            else:
                data[key] = None
        return data

    @staticmethod
    def searchBySingleString(cls, fields, word):
        """
        Search for database entries matching a single word in specified fields.

        This method searches for entries in the database table corresponding to
        the provided class. It uses the provided fields and word to construct
        filters for the database query. The method returns instances of the
        specified class populated with data matching the filters.

        :param cls: The class corresponding to the database table to be queried.
        :type cls: Type
        :param fields: A list of field names to search within.
        :type fields: list[str]
        :param word: The word to search for within the specified fields.
        :type word: str
        :return: A list of instances of the specified class populated with data
                 matching the search filters.
        :rtype: list[Type]
        """
        drv: Driver = getDriver(Config().get("DATABASE_DRIVER")).Database()
        filters = {}
        for field in fields:
            filters[field] = word
        data = drv.search(cls, filters)
        objects = []
        if data is None:
            return objects
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


    @staticmethod
    def getMany(cls, key, value):
        """
        Fetches multiple records from the database matching the given key and value,
        then converts and returns them as a list of objects of the specified class.

        :param cls: The class type to instantiate and populate with the fetched data.
        :type cls: Type
        :param key: The key (field name) to filter the records in the database.
        :type key: str
        :param value: The value corresponding to the key to filter records.
        :type value: Any
        :return: List of objects of type `cls` with attributes set from the fetched data.
        :rtype: list
        """
        drv: Driver = getDriver(Config().get("DATABASE_DRIVER")).Database()
        data = drv.get(cls, {key:value}, limit=None)
        objects = []
        if data is None:
            return objects
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
        """
        Provides a class method to retrieve the name of the table.

        This method generates a table name based on the class name by converting the class
        name to lowercase and appending an 's' to it. It is typically used in ORM (Object
        Relational Mapping) frameworks to determine the corresponding table name for a class.

        :rtype: str
        :return: Lowercase string of the class name with an appended 's'.
        """
        return str.lower(cls.__name__) + "s"

    # RELATIONS

    def hasOne(self, object):
        """
        Determine the associated object based on the naming convention of the attribute.

        A 'hasOne' relationship is inferred by constructing the attribute name in the form of
        '{lower case class name}_id'. This attribute is expected to exist in the current instance.
        The corresponding object is then fetched using the `get` method of the provided class,
        given the value of this attribute.

        :param object: The class of the related object. A new instance of this class is created
                       and the `get` method is called on it with the id value.
        :type object: type
        :return: An instance of the related object, fetched by the id attribute from the current instance.
        :rtype: object
        """
        field_name = str.lower(object.__name__) + "_id"
        object_id = getattr(self, field_name)
        return object().get(object_id)

    def belongsToMany(self, object):
        """
        Determines if the current instance belongs to many of the given objects.

        Constructs a row name using the class name of the current instance
        in lowercase followed by "_id". Then, it utilizes the `getMany` method
        of the provided object to determine the relationship.

        :param object: The object to compare against.
        :type object: Any
        :return: A result from the `getMany` method of the provided object.
        :rtype: Any
        """
        row_name = str.lower(self.__class__.__name__) + "_id"
        return object.getMany(object, row_name, self.id)

    @staticmethod
    def filterCollectionBy(collection: table, filters):
        """
        Filters a collection of items based on specified filter criteria provided in the
        filters dictionary.

        This method iterates through each item in the provided collection and checks if
        it satisfies all the filter criteria specified in the filters dictionary. If an
        item satisfies all the criteria, it is added to the return_collection list.

        :param collection: The collection of items to be filtered.
        :type collection: table
        :param filters: A dictionary containing filter criteria where keys are the
                        attribute names and values are the required values of these attributes.
        :type filters: dict
        :return: A list containing items from the collection that meet all the filter
                 criteria.
        :rtype: list
        """
        return_collection = []
        for item in collection:
            filters_fullfill = True
            for filter in filters.keys():
                if getattr(item, filter) != filters[filter]:
                    filters_fullfill = False
            if filters_fullfill:
                return_collection.append(item)
        return return_collection




