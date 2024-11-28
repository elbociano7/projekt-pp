import datetime
import tkinter
from tkinter import StringVar, Label, Button, Entry, Frame
from tkinter.ttk import Treeview

from src.ui.translations import Tr
from src.ui.view import View
from src.ui.views import helpers
from src.ui.views.helpers import Heading


class VTemplate(View):
    firstname = StringVar()
    lastname = StringVar()

    def onSaveClick(self):
        pass

    def onCancelClick(self):
        pass

    def buildView(self, master):
        Label(master, text=Tr('firstname')).pack()
        Entry(master, textvariable=self.firstname).pack()
        Label(master, text=Tr('firstname')).pack()
        Entry(master, textvariable=self.lastname).pack()

        buttons = Frame(master)

        Button(buttons, text=Tr('add'), command=self.onSaveClick).grid(row=0, column=0)
        Button(buttons, text=Tr('cancel'), command=self.onCancelClick).grid(row=0, column=1)

        buttons.pack(fill='x', pady = 10, padx=20)






