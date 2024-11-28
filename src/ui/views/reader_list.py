import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame

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
            Label(
                frame,
                text = f"{result['firstname']} {result['lastname']}",
                justify='left',
                width=40
            ).pack(side=tkinter.LEFT, padx = 2, anchor=tkinter.W)
            Button(
                frame,
                text=f"Wybierz ({result['id']})",
                command=lambda r_id=result['id']: self.onEditClick(r_id),
            ).pack(side=tkinter.RIGHT, padx = 2, anchor=tkinter.W)
            frame.pack()

    def buildView(self, master):
        if not self.loan:
            Button(
                master,
                text='Wyszukiwanie ksiazek',
                command=self.onChangeSearchClick,
                width=180,
            ).pack(side=tkinter.TOP, anchor=tkinter.N, pady = (0, 20), padx = 5)
        Label(
            master,
            text='Wyszukaj czytelnika (imię, nazwisko lub id)',
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
        self.frame = Frame(master, height=100, width=180)
        self.frame.pack(padx=5, pady=5)
