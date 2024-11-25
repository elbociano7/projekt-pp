class Config:

  configuration = {
    "DEBUG": False,
    "API_DRIVER": "google",
    "DATABASE_DRIVER": "database",
    "DATABASE_HOST": "localhost",
    "DATABASE_PORT": "3303",
    "DATABASE_USER": "root",
    "DATABASE_PASSWORD": "",
    "DATABASE_NAME": "dane",
    "DEFAULT_BOOK_COUNT": 10,
    "STORE_BOOKS_LOCALLY": True,
    "PAGINATION_LIMIT": 50
  }

  def get(self, key: str) -> any:
    """Get configuration key's value

    Args:
        key (str): Key

    Returns:
        any: Configuration value
    """
    return self.configuration[key]

CONFIG = Config()