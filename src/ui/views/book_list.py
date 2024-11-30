import copy
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame

from src.ui.translations import Tr
from src.ui.view import View

class VTemplate(View):
    searchStr = StringVar()

    book_title = ''

    frame = None

    loan = False

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
            frame.columnconfigure(0, weight=10, uniform='name')
            frame.columnconfigure(1, weight=1, uniform='name')
            Label(
                frame,
                text=f"{result['author']} - {result['title']} ({result['year']})",
                justify='left', wraplength=800
            ).grid(row=0, column=0, padx = 2, sticky=tkinter.W)
            Button(
                frame,
                text="Wybierz",
                command=lambda r_id=result['id']: self.onEditClick(r_id),
            ).grid(row=0, column=1, padx = 2, sticky=tkinter.W)
            frame.pack(fill='x')


    def buildView(self, master):
        if not self.loan:
            Button(
                master,
                text=Tr('search_reader'),
                command=self.onChangeSearchClick,
                width=180,
            ).pack(side=tkinter.TOP, anchor=tkinter.N, pady = (0, 20), padx = 5)
        Label(
            master,
            text=Tr('search_book_str'),
            width=180
        ).pack(padx=5, pady=1)
        Entry(
            master,
            textvariable=self.searchStr,
            width=180,
        ).pack(padx=5, pady=1)
        Button(
            master,
            text=Tr('search'),
            command=self.onSearchClick,
            width=180,
        ).pack(padx=5, pady=1)
        self.frame = Frame(master, height=100, width=180)
        self.frame.pack(padx=5, pady=5)

