import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame

from src.ui.translations import Tr
from src.ui.view import View

class VTemplate(View):
    """
    Example view template class.
    Not actually used in the application.
    """

    # Variable that is accessible from controller.
    field_str = StringVar()

    @staticmethod
    def onSearchClick():
        """
        Empty method used for handling search click event.
        This method should be overridden by controller object.
        :return:
        """
        pass

    def setResults(self, results):
        """
        Method used for displaying search results.
        If onSearchClick is overridden, it should finally point to this method to display processed results.
        Search button -> onSearchClick [overriden] -> some search logic -> setResults -> UI

        :param results: Custom parameter
        :return:
        """
        # Code responsible for displaying search results in UI
        pass

    def buildView(self, master):
        """
        Main method used for building an interface. In this method, almost all widgets should be created
        (dynamic widgets can be created in e.g. setResults method). Mehtod is called once on build view
        with master window object in parameter.
        :param master: Master widger for tkinter modules
        :return:
        """


