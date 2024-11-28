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
    reader = {}

    days = StringVar()

    def onSaveClick(self):
        print(self.days.get())

    def onCancelClick(self):
        pass

    def buildView(self, master):
        Heading(master, Tr('book'))
        helpers.makeTable(self.book, master)
        Heading(master, Tr('reader'))
        helpers.makeTable(self.reader, master)

        self.days.set('30')

        Label(master, text=Tr('loan_timespan')).pack(pady=(3, 10))
        tkinter.Spinbox(master, from_=1, to=365, textvariable=self.days).pack()

        buttons = Frame(master)

        Button(buttons, text=Tr('loan'), command=lambda d=self.days.get(): self.onSaveClick(d)).grid(row=0, column=0)
        Button(buttons, text=Tr('cancel'), command=self.onCancelClick).grid(row=0, column=1)

        buttons.pack(fill='x', pady = 10, padx=20)





