import importlib


class View:
    """
    The View class is responsible for loading and building UI views.

    This class allows for the dynamic loading of UI views by specifying the module
    name and provides a method to build the view on a given master widget. This can
    be particularly useful in applications with modular views where the specific
    view to display may change at runtime.

    :ivar attribute1: Description of attribute1.
    :type attribute1: type
    :ivar attribute2: Description of attribute2.
    :type attribute2: type
    """
    @staticmethod
    def Load(view: str):
        """
        Loads and returns the specified view module.

        The specified view module is imported dynamically using the view name
        provided as a parameter. The module's VTemplate class is then instantiated
        and returned. This function is for loading user interface views based on
        their names, facilitating a plugin-like architecture.

        :param view: The name of the view module to be loaded. The function expects
            the view name to be a string corresponding to a module path under
            'src.ui.views'.
        :type view: str
        :return: An instance of the VTemplate class from the specified view module.
        :rtype: VTemplate
        """
        view = importlib.import_module(f"src.ui.views.{view}")
        return view.VTemplate()

    def buildView(self, master):
        """
        Constructs and initializes the view within the given master widget.

        :param master: The parent widget within which the view is to be constructed.
        :type master: Widget
        :return: None
        """
        pass

