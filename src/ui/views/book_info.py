import datetime
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame
from tkinter.ttk import Treeview

from src.ui.translations import Tr
from src.ui.view import View
from src.ui.views import helpers
from src.ui.views.helpers import Heading


class VTemplate(View):
    book = {}
    loans = []

    @staticmethod
    def onBackClick():
        pass

    @staticmethod
    def onSaveClick(book_id, data):
        pass

    @staticmethod
    def onLoanClick():
        pass

    @staticmethod
    def returnBook():
        pass

    available = False

    def buildView(self, master):
        table_data = {}
        for key in self.book.keys():
            table_data[key] = self.book[key]
        helpers.makeTable(table_data, master)

        # AKTYWNE WYPOZYCZENIA
        Heading(master, text=Tr('active_loans'))

        loans_columns = ('loan_id', 'reader', 'start_date', 'end_date')
        treeview = Treeview(master, columns=loans_columns, show='headings')
        treeview.tag_configure('expired', foreground='red')
        treeview.column('loan_id', width=60, anchor='center')
        treeview.column('reader', width=100, anchor='center')
        treeview.column('start_date', width=150, anchor='center')
        treeview.column('end_date', width=150, anchor='center')
        for col in loans_columns:
            treeview.heading(col, text=Tr(col))

        for loan in self.loans:
            if loan['returned'] == 0:
                id = loan['id']

                expired = loan['end_date'] < datetime.datetime.now()

                treeview.insert(
                    "",
                    tkinter.END,
                    text=id,
                    values=(loan['id'], loan['reader'], loan['start_date'], loan['end_date']),
                    tags=(('expired',) if expired else ('ongoing',))
                )

        treeview.pack(fill='x')

        def returnBooks():
            for item in treeview.selection():
                self.returnBook(treeview.item(item)['values'][0])
                treeview.delete(item)

        buttons = Frame(master)
        (Button(buttons,
               text=Tr('back'),
               command = self.onBackClick)
         .grid(row=0, column=0))
        (Button(buttons,
               text=Tr('loan'),
               state=tkinter.NORMAL if self.available else tkinter.DISABLED, #None if self.available else '#777'
               command=self.onLoanClick)
         .grid(row=0, column=1))
        returnButton = Button(buttons,
                              text=Tr('return'),
                              command=returnBooks,
                              state=tkinter.DISABLED)
        returnButton.grid(row=0, column=2)

        def changeButtonState(event):
            if treeview.selection():
                returnButton.config(state=tkinter.NORMAL)
            else:
                returnButton.config(state=tkinter.DISABLED)

        treeview.bind('<<TreeviewSelect>>', changeButtonState)
        buttons.pack(fill='x')



