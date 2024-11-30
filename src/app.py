from src.configuration import CONFIG
from src.drivers.driver import getDriver, DriverException
from src.ui.ui import MainWindow, Window
from src.ui.view import View


class App:
  """
  The App class represents the core application framework.

  This class handles initialization of the main window and controls the
  flow of the application by managing views and routing.

  :ivar main_window: The main window instance of the application.
  :type main_window: MainWindow
  """
  def __init__(self):
    """App initialization
    """
    self.main_window = MainWindow()

  def run(self):
    """
    Represents the main application which initializes the main window and routing procedures.

    This class is responsible for starting the main UI window and setting up the routing
    mechanism using a `RoutingController`.
    """

    db = getDriver(CONFIG.get('DATABASE_DRIVER')).Database()
    try:
      db.checkDatabase()
    except DriverException as e:
      Window.makeErrorMessageBox('error', str(e))
      return

    from src.controllers.routing import RoutingController
    self.main_window.open()

    router = RoutingController()
    router.run(self)

  def view(self, view):
    """
    Manages the views in the main window.

    :param view: The view to be displayed in the main window.
    :type view: View
    :return: None
    """
    self.main_window.loadView(view)
