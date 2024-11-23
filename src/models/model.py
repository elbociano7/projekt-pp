from ..drivers.driver import Driver
from ..configuration import Config

class Model:
  table: str = ""
  id: int = None
  readonly: bool = False
  driver: str = Config().get("DATABASE_DRIVER")

  def getByField(self, field: str, value: any, driver: str):
    drv = Driver(driver)
    return drv.get(field, value, self)
  
  def get(self, id: int):
    return self.findByField("id", id)

  @classmethod
  def getTableName(cls):
    return str.lower(cls.__name__)+"s"
  

  # RELATIONS

  def hasOne(self, object: str):
    field_name = str.lower(object.__class__)+"_id"
    object_id = getattr(object, field_name)
    return object.find(object_id)

  def belongsToMany(self, object: str):
    field_name = str.lower(self.__class__)+"_id"
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  TODO
    
  