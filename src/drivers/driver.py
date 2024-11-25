import importlib


def getDriver(driver):
  print("starting driver: ", driver)
  return importlib.import_module(f"src.drivers.{driver}.main")

class Driver:
  def get(self, modelClass, filters, limit):
    return False
  def insert(self, object):
    return False
  def update(self, object):
    return False

class DriverException(Exception):
  pass