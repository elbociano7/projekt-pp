from datetime import datetime, timedelta
from tkinter import messagebox

from src.configuration import CONFIG
from src.controllers.controller import Controller
from src.models.book import Book, BookSearchException
from src.models.loan import Loan
from src.models.reader import Reader
from src.ui.translations import Tr
from src.ui.view import View


class BookController(Controller):

    @staticmethod
    def list(router, params):
        """
        List all books

        :param router: RouteController
        :return: None
        """

        view = View.Load('book_list')
        view.onChangeSearchClick = lambda: router.changeRoute('reader_list')

        def openView(book_id):
            router.changeRoute('book_info', {'book_id': book_id})

        view.onEditClick = openView

        def prepareSearch():
            search = view.searchStr.get()
            try:
                objects = Book.searchBySingleString(Book, ('id', 'title', 'author', 'year'), search)
            except BookSearchException as e:
                messagebox.showerror(Tr('error'), Tr(str(e)))
                return
            results = []
            for book in objects:
                data = book.serialize()
                results.append(data)
            view.setResults(results)

        view.onSearchClick = prepareSearch

        view.onEditClick = openView

        router.app.view(view)

    @staticmethod
    def viewBook(router, params):
        """
        Create and handle view for book info
        :param router:
        :param params:
        :return:
        """
        view = View.Load('book_info')
        book = Book()
        book.get(params['book_id'])
        view.book = book.serialize()
        loans = book.loans()
        view.loans = []
        for loan in loans:
            reader = Reader()
            reader.get(loan.reader_id)
            data = loan.serialize()
            data['reader'] = f"{reader.firstname} {reader.lastname}"
            view.loans.append(data)

        def back():
            router.changeRoute('book_list')

        view.onBackClick = back

        def returnBook(loan_id):
            loan = Loan()
            loan.get(loan_id)
            loan.returned = True
            loan.save()

        def afterReturn():
            if CONFIG.get("RELOAD_AFTER_RETURN"):
                router.changeRoute('book_info', {'book_id': book.id})

        view.returnBook = returnBook
        view.afterReturn = afterReturn



        if book.isAvailable():
            view.available = True
            def loan():
                router.changeRoute('reader_list', {'action': 'loan', 'book_id': book.id})
            view.onLoanClick = loan

        router.app.view(view)

    @staticmethod
    def loanBook(router, params):

        view = View.Load('book_loan')

        book = Book().get(params['book_id'])
        reader = Reader().get(params['reader_id'])

        def goBack():
            router.changeRoute('book_info', {'book_id': book.id})

        def loanBook(days):
            if not days.isdigit() or int(days) < 1 or int(days) > 999:
                messagebox.showerror(Tr('error'), Tr('invalid_days'))
                return
            end_time = datetime.now() + timedelta(days=int(days))
            end_time = end_time.replace(hour=23, minute=59, second=58)
            reader.loanBook(book, end_time)
            goBack()

        view.onSaveClick = loanBook
        view.onCancelClick = goBack

        view.book = book.serialize()
        view.reader = reader.serialize()

        router.app.view(view)

