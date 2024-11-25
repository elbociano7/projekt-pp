from src.models.model import Model

class Reader(Model):

  serializable = ['id', 'firstname', 'lastname']

  def loans(self):
    from src.models.loan import Loan
    return self.belongsToMany(Loan)


  