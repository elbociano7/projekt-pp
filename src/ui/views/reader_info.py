import datetime
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame
from tkinter.ttk import Treeview

from src.ui.translations import Tr
from src.ui.view import View
from src.ui.views import helpers


class VTemplate(View):
    reader = {}
    loans = []

    @staticmethod
    def onBackClick():
        pass

    @staticmethod
    def onSaveClick(reader_id, data):
        pass

    @staticmethod
    def onLoanClick():
        pass

    @staticmethod
    def returnBook(loan_id):
        pass

    available = False

    def buildView(self, master):
        table_data = {}
        for key in self.reader.keys():
            table_data[key] = self.reader[key]
        helpers.makeTable(table_data, master)

        # AKTYWNE WYPOZYCZENIA
        Label(master, text="Aktywne wypozyczenia").pack(padx=10, pady=10)

        loans_columns = ('loan_id', 'book', 'start_date', 'end_date')
        treeview = Treeview(master, columns=loans_columns, show='headings')
        treeview.tag_configure('expired', foreground='red')
        treeview.column('loan_id', width=60, anchor='center')
        treeview.column('book', width=100, anchor='center')
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
                     values=(loan['id'], loan['book'], loan['start_date'], loan['end_date']),
                     tags=(('expired',) if expired else ('ongoing',))
                 )

        # for loan in self.loans:
        #
        #         id = loan['id']
        #
        #
        #
        #

        treeview.pack(fill='x')

        buttons = Frame(master)

        def returnBooks():
            for item in treeview.selection():
                self.returnBook(treeview.item(item)['values'][0])
                treeview.delete(item)

        (Button(buttons,
               text="Powrot",
               command = self.onBackClick)
         .grid(row=0, column=0))
        returnButton = Button(buttons,
            text="Zwrot",
            command=returnBooks,
            state=tkinter.DISABLED)
        returnButton.grid(row=0, column=1)

        def changeButtonState(event):
            if treeview.selection():
                returnButton.config(state=tkinter.NORMAL)
            else:
                returnButton.config(state=tkinter.DISABLED)

        treeview.bind('<<TreeviewSelect>>', changeButtonState)

        buttons.pack(fill='x')



