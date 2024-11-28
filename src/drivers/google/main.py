from src.drivers.driver import Driver
from src.drivers.google.worker import ApiWorker


class Api(Driver):

    def get(self, objectClass, filters):
        """
        Not supported in this API
        :param objectClass:
        :param filters:
        :return:
        """
        raise Exception("Unsupported API usage")
    def insert(self, object):
        """
        Not supported in this API
        :param object:
        :return:
        """
        raise Exception("Unsupported API usage")
    def update(self, object):
        """
        Not supported in this API
        :param object:
        :return:
        """
        raise Exception("Unsupported API usage")
    def search(self, classObject, filters):
        """Not supported in this API"""
        raise Exception("Unsupported API usage")
    def searchSingleWord(self, objectClass, word):
        """
        Search for an item with a single string of search terms
        :param objectClass: Used for compatibility
        :param filters: search terms
        :return array: Search results
        """
        return ApiWorker().searchItem(word)