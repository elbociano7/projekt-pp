import datetime
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame
from tkinter.ttk import Treeview

from PIL import ImageTk, Image

from src.ui.translations import Tr
from src.ui.view import View
from src.ui.views import helpers
from src.ui.views.helpers import Heading
from src.ui.webimage import WebImage


class VTemplate(View):
    book = {}
    reader = {}

    days = StringVar()

    @staticmethod
    def onSaveClick(days):
        pass

    def onCancelClick(self):
        pass

    def buildView(self, master):
        #Display book and reader data
        book_data = self.book
        if 'image' in book_data.keys():
            img = book_data['image']
        else:
            img = None
        book_data.pop('image')
        Heading(master, Tr('book'))

        ##BOOK IMAGE WITH DATA

        dataframe = Frame(master)
        dataframe.columnconfigure(0, weight=0)
        dataframe.columnconfigure(1, weight=2)
        tableframe = Frame(dataframe)
        helpers.makeTable(book_data, tableframe, image=True)

        img = Image.open(WebImage.get(img))

        imgtk = ImageTk.PhotoImage(img.resize((80, 120)))
        imglabel = Label(dataframe, image=imgtk)
        imglabel.image = imgtk
        imglabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        tableframe.grid(row=0, column=1, sticky='w')
        dataframe.pack(fill='x')

        Heading(master, Tr('reader'))
        helpers.makeTable(self.reader, master)

        #Loan days input

        self.days.set('30')

        Label(master, text=Tr('loan_timespan')).pack(pady=(3, 10))
        tkinter.Spinbox(master, from_=1, to=365, textvariable=self.days).pack()

        #Buttons

        def loanClick():
            self.onSaveClick(self.days.get())

        buttons = Frame(master)

        Button(buttons, text=Tr('loan'), command=loanClick).grid(row=0, column=0)
        Button(buttons, text=Tr('cancel'), command=self.onCancelClick).grid(row=0, column=1)

        buttons.pack(fill='x', pady = 10, padx=20)






