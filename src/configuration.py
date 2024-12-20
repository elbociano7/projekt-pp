import os


class Config:
  """
  Configuration class
  """

  #Main configuration data
  configuration = {
    # API
    "API_DRIVER": "google", # Default 'google'
    "API_URL": "https://www.googleapis.com/", # Default 'https://www.googleapis.com/'

    # DATABASE
    "DATABASE_DRIVER": "database", # Default 'database'
    "DATABASE_HOST": "localhost",
    "DATABASE_PORT": "3306",
    "DATABASE_USER": "root",
    "DATABASE_PASSWORD": "",
    "DATABASE_NAME": "pp-data",

    # BOOK CONFIGURATION
    "DEFAULT_BOOK_COUNT": 10, # Default 10

    # FORCE RELOAD VIEW AFTER RETURNING A BOOK
    "RELOAD_AFTER_RETURN": True, # True is program-bug-safe, False is More-tkinter-bugless-friendly

    # PATHS
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