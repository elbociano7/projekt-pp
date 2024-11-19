class Config:
  configuration = {
    "API_DRIVER": "google"
  }

  def get(self, key: str):
    return self.configuration[key]