from datetime import datetime
from pyexpat.errors import messages
from re import search

from src.configuration import CONFIG
from src.controllers.controller import Controller
from src.models.book import Book
from src.models.loan import Loan
from src.models.reader import Reader
from src.ui.translations import Tr
from src.ui.ui import Window
from src.ui.view import View


class ReaderController(Controller):
    @staticmethod
    def list(router, params = {}):

        view = View.Load('reader_list')
        view.onChangeSearchClick = lambda: router.changeRoute('book_list')

        def openView():
            pass

        add = None

        open_view = lambda reader_id: router.changeRoute('reader_info', {'reader_id': reader_id})
        add = lambda: router.changeRoute('reader_add')

        prepare_search_string = None

        if type(params) is dict:
            if 'action' in params and params['action'] == 'loan':
                view.loan = True
                view.goBack = lambda: router.changeRoute('book_info', {'book_id': params['book_id']})
                open_view = lambda reader_id, book_id = params['book_id']: router.changeRoute('book_loan', {'reader_id': reader_id, 'book_id': book_id})
                add = lambda: router.changeRoute('reader_add', {'action': 'loan', 'book_id': params['book_id']})
            if 'search' in params and params['search'] != '' and params['search'] is not None:
                prepare_search_string = params['search']

        view.onEditClick = open_view

        view.onAddClick = add

        def prepareSearch(custom_string = None):
            search = ''
            if custom_string is None:
                search = view.searchStr.get()
            else:
                search = custom_string
            objects = Reader.searchBySingleString(Reader, ('id', 'firstname', 'lastname'), search)
            results = []
            for reader in objects:
                data = reader.serialize()
                results.append(data)
            view.setResults(results)

        view.onSearchClick = prepareSearch

        view.onEditClick = open_view

        view.on_start_search = prepare_search_string

        router.app.view(view)

    @staticmethod
    def readerInfo(router, params):
        view = View.Load('reader_info')
        reader = Reader()
        reader.get(params['reader_id'])
        view.reader = reader.serialize()
        loans = reader.loans()
        view.loans = []
        for loan in loans:
            book = Book()
            book.get(loan.book_id)
            data = loan.serialize()
            data['book'] = f"{book.title} - {book.author}"
            view.loans.append(data)

        def back():
            router.changeRoute('reader_list')

        view.onBackClick = back

        def returnBook(loan_id):
            loan = Loan()
            loan.get(loan_id)
            loan.returned = True
            loan.save()
            if CONFIG.get("RELOAD_AFTER_RETURN"):
                router.changeRoute('reader_info', {'book_id': reader.id})

        view.returnBook = returnBook

        router.app.view(view)

    @staticmethod
    def readerAdd(router, params):
        view = View.Load('reader_add')

        back = None

        if type(params) is not dict:
            back = lambda string = '': router.changeRoute('reader_list', {'search': string})
        elif params['action'] == 'loan':
            back = lambda string = '': router.changeRoute('reader_list', {"action": "loan", "book_id": params['book_id'], 'search': string})

        def save():
            reader = Reader()
            reader.firstname = view.firstname.get()
            reader.lastname = view.lastname.get()

            if(reader.firstname == '' or reader.lastname == ''):
                Window.makeErrorMessageBox(Tr('error'), Tr('empty_fields'))
                return

            reader.save()
            back(f"{str(reader.id)} {reader.firstname} {reader.lastname}")

        view.onSaveClick = save

        view.onCancelClick = back

        router.app.view(view)