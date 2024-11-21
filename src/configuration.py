class Config:

  configuration = {
    "DEBUG": False,
    "API_DRIVER": "google",
    "DATABASE_DRIVER": "database",
    "DEFAULT_BOOK_COUNT": 10,
    "STORE_BOOKS_LOCALLY": True,
  }

  def get(self, key: str) -> any:
    """Get configuration key's value

    Args:
        key (str): Key

    Returns:
        any: Configuration value
    """
    return self.configuration[key]