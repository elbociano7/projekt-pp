from src.app import App
from src.controllers.controller import Controller
from src.controllers.reader import ReaderController
from src.ui.view import View


class RoutingController(Controller):

    app: App = None

    from src.controllers.book import BookController
    routes = {
        'book_list': BookController.list,
        'book_info': BookController.viewBook,
        'book_loan': BookController.loanBook,
        'reader_list': ReaderController.list,
        'reader_info': ReaderController.readerInfo,
        'reader_add': ReaderController.readerAdd,
    }

    route = None

    defaultRoute = 'book_list'

    def run(self, app: App):
        self.app = app
        self.changeRoute(self.defaultRoute)

    def changeRoute(self, route, params = None):
        self.route = route
        self.routes[route](self, params)
