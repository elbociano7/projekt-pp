from src.drivers.driver import Driver


class Api(Driver):
    def __init__(self):
        print('googleDriver')

    def get(self, objectClass, filters):
        return {'title': 'gd', 'id': 12}
    def insert(self, object):
        return False
    def update(self, object):
        return False
    def search(self, objectClass, filters):
        return 'gd'