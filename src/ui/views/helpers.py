import tkinter
from tkinter import Frame, Label

from src.ui.translations import Tr

"""
UI HELPER FUNCTIONS FILE
"""

def makeTable(data, master, image = False):
    """
    Generates a table from provided data and displays it within the given master widget.

    :param data: A dictionary where keys are used as row labels and values
        are used as the corresponding data in the table
    :type data: dict
    :param master: The parent widget where the table will be displayed
    :type master: tkinter.Widget
    :return: None
    """
    table = Frame(master)
    table.grid_columnconfigure(0, weight=2, uniform='a')
    if image is False:
        table.grid_columnconfigure(1, weight=2, uniform='a')
    else:
        table.grid_columnconfigure(1, weight=3, uniform='a')
    i = 0
    for key in data.keys():
        tlb = Label(table, text = Tr(key), justify=tkinter.LEFT, foreground="#999")
        tlb.grid(row=i, column = 0, sticky=tkinter.E)
        dlb = Label(table, text = data[key], justify=tkinter.LEFT, wraplength=300)
        dlb.grid(row=i, column = 1, sticky=tkinter.W)
        i += 1
    table.pack(fill='x')

def Heading(master, text):
    lb = Label(master, text=Tr(text), font=('Arial', 20))
    lb.pack(
        fill='x', pady=(3, 10)
    )
    return lb
