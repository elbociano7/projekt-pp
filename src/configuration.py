import os


class Config:
  """
  Configuration class
  """

  #Main configuration data
  configuration = {
    "DEBUG": False,
    "API_DRIVER": "google",
    "API_URL": "https://www.googleapis.com/",
    "DATABASE_DRIVER": "database",
    "DATABASE_HOST": "localhost",
    "DATABASE_PORT": "3301",
    "DATABASE_USER": "root",
    "DATABASE_PASSWORD": "",
    "DATABASE_NAME": "dane",
    "DEFAULT_BOOK_COUNT": 10,
    "STORE_BOOKS_LOCALLY": True,
    "PAGINATION_LIMIT": 50,
    "BASE_APP_PATH": os.path.dirname(os.path.realpath(__file__)),
    "CACHE_PATH": os.path.dirname(os.path.realpath(__file__)) + "/cache",
  }

  def get(self, key: str) -> any:
    """Get configuration key's value

    :param key str: configuration key
    :return any: configuration value
    """
    return self.configuration[key]

#Glocal config object
CONFIG = Config()