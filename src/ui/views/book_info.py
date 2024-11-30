import datetime
import io
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame, PhotoImage, TclError
from tkinter.ttk import Treeview
from PIL import Image, ImageTk

from src.configuration import CONFIG
from src.ui.translations import Tr
from src.ui.view import View
from src.ui.views import helpers
from src.ui.views.helpers import Heading
from src.ui.webimage import WebImage


class VTemplate(View):
    book = {}
    loans = []

    returnButton = None

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
    def returnBook(book):
        pass

    @staticmethod
    def afterReturn():
        pass

    available = False

    def buildView(self, master):
        dataframe = Frame(master)
        dataframe.columnconfigure(0, weight=0)
        dataframe.columnconfigure(1, weight=2)
        tableframe = Frame(dataframe)
        table_data = {}
        for key in self.book.keys():
            table_data[key] = self.book[key]
        table_data.pop('image')
        helpers.makeTable(table_data, tableframe, image=True)

        img = Image.open(WebImage.get(self.book['image']))

        imgtk = ImageTk.PhotoImage(img.resize((80, 120)))
        imglabel = Label(dataframe, image=imgtk)
        imglabel.image = imgtk
        imglabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        tableframe.grid(row=0, column=1, sticky='w')
        dataframe.pack(fill='x')

        # AKTYWNE WYPOZYCZENIA
        Heading(master, text=Tr('active_loans'))

        loans_columns = ('loan_id', 'reader', 'reader_id', 'start_date', 'end_date')
        treeview = Treeview(master, columns=loans_columns, show='headings')
        treeview.tag_configure('expired', foreground='red')
        treeview.column('loan_id', width=100, anchor='center')
        treeview.column('reader_id', width=100, anchor='center')
        treeview.column('reader', width=300, anchor='center')
        treeview.column('start_date', width=200, anchor='center')
        treeview.column('end_date', width=200, anchor='center')
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
                    values=(loan['id'], loan['reader'], loan['reader_id'], loan['start_date'], loan['end_date']),
                    tags=(('expired',) if expired else ('ongoing',))
                )

        treeview.pack(fill='x')

        def returnBooks():
            selection = treeview.selection()
            for item in selection:

                self.returnBook(treeview.item(item)['values'][0])
                try:
                    treeview.delete(item)
                except TclError:
                    print('Tkinter error')
            self.afterReturn()

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



