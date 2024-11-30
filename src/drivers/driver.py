import importlib


def getDriver(driver):
  """
  Returns a driver instance
  :param str: driver name
  :return:
  """
  return importlib.import_module(f"src.drivers.{driver}.main")

class Driver:
  """
  Basic data driver methods
  """
  def get(self, modelClass, filters, limit):
    return False
  def insert(self, object):
    return False
  def update(self, object):
    return False

class DriverException(Exception):
  pass