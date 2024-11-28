from datetime import datetime

from src.controllers.controller import Controller
from src.models.book import Book
from src.models.loan import Loan
from src.models.reader import Reader
from src.ui.view import View


class ReaderController(Controller):
    @staticmethod
    def list(router, params):

        view = View.Load('reader_list')
        view.onChangeSearchClick = lambda: router.changeRoute('book_list')

        def openView():
            pass


        if type(params) is not dict:
            openView = lambda reader_id: router.changeRoute('reader_info', {'reader_id': reader_id})
        elif params['action'] == 'loan':
            view.loan = True
            openView = lambda reader_id, book_id = params['book_id']: router.changeRoute('book_loan', {'reader_id': reader_id, 'book_id': book_id})

        view.onEditClick = openView

        def add():
            router.changeRoute('reader_add')

        view.onAddClick = add

        def prepareSearch():
            search = view.searchStr.get()
            objects = Reader.searchBySingleString(Reader, ('id', 'firstname', 'lastname'), search)
            results = []
            for reader in objects:
                data = reader.serialize()
                results.append(data)
            print(results)
            view.setResults(results)

        view.onSearchClick = prepareSearch

        view.onEditClick = openView

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

        view.returnBook = returnBook

        # if book.isAvailable():
        #     view.available = True
        #
        #     def loan():
        #         print('loan')
        #
        #     view.onLoanClick = loan

        router.app.view(view)

    @staticmethod
    def readerAdd(router, params):
        view = View.Load('reader_add')

        def save():
            reader = Reader()
            reader.firstname = view.firstname.get()
            reader.lastname = view.lastname.get()
            reader.save()
            router.changeRoute('reader_list')

        view.onSaveClick = save

        def cancel():
            router.changeRoute('reader_list')

        view.onCancelClick = cancel

        router.app.view(view)