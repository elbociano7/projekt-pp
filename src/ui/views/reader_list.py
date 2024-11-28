import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame

from src.ui.translations import Tr
from src.ui.view import View

class VTemplate(View):
    """
    A view template class for a book search and edit interface.

    This class is used to create a UI for searching and editing book entries.
    It contains methods to handle search actions, edit actions, and dynamically
    update the search results on the interface.

    :ivar searchStr: A StringVar instance to bind the entry widget for search input.
    :type searchStr: StringVar
    :ivar frame: A Frame instance to contain the search results.
    :type frame: Frame or None
    """
    searchStr = StringVar()

    loan = False

    def __init__(self):
        self.frame = None

    @staticmethod
    def onSearchClick():
        pass

    @staticmethod
    def onAddClick():
        pass

    @staticmethod
    def onEditClick(book_id):
        pass

    @staticmethod
    def onChangeSearchClick():
        pass

    def setResults(self, results):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for result in results:
            frame = Frame(self.frame)
            frame.columnconfigure(0, weight=1, uniform='name')
            frame.columnconfigure(1, weight=0, uniform='name')
            Label(
                frame,
                text = f"{result['firstname']} {result['lastname']}",
                justify='left',
            ).grid(row=0, column=0, padx = 2, sticky=tkinter.W)
            Button(
                frame,
                text=Tr('select'),
                command=lambda r_id=result['id']: self.onEditClick(r_id),
            ).grid(row=0, column=1, padx = 2, sticky=tkinter.W)
            frame.pack(fill='x')

    def buildView(self, master):
        if not self.loan:
            Button(
                master,
                text=Tr('search_book'),
                command=self.onChangeSearchClick,
                width=180,
            ).pack(side=tkinter.TOP, anchor=tkinter.N, pady = (0, 20), padx = 5)
        Label(
            master,
            text=Tr('search_reader_str'),
            width=180
        ).pack(padx=5, pady=1)
        Entry(
            master,
            textvariable=self.searchStr,
            width=180,
        ).pack(padx=5, pady=1)
        Button(
            master,
            text='Szukaj',
            command=self.onSearchClick,
            width=180,
        ).pack(padx=5, pady=1)
        Button(
            master,
            text='Dodaj',
            command=self.onAddClick,
            width=180,
        ).pack(padx=5, pady=1)
        self.frame = Frame(master, height=100, width=180)
        self.frame.pack(padx=5, pady=5)