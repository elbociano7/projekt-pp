from tkinter import Label

import tkinter

from src.ui.view import View

class Window:
    """
    Manages the main application window's properties and behavior.

    Detailed description of the class, its purpose, and usage.

    :ivar title: Title of the window.
    :type title: str
    :ivar style: Dictionary containing style attributes like background color,
                 minsize, maxsize, and geometry of the window.
    :type style: dict
    :ivar root: Main Tkinter window object.
    :type root: tkinter.Tk
    :ivar main_frame: Main frame within the root window where views are loaded.
    :type main_frame: tkinter.Frame
    :ivar running: Boolean flag indicating whether the main loop is running.
    :type running: bool
    """
    title = "Window"
    style = {
        'background': None,
        'minsize': (900,500),
        'maxsize': (900,500),
        'geometry': "900x500+50+50"
    }
    root = tkinter.Tk()
    main_frame = tkinter.Frame(root)
    running = False

    def open(self, title: str = None):
        """
        Opens the main application window with the given title and applies styles.

        This method sets the title of the main application window to the provided
        title, or uses the stored title if none is provided. It configures the
        background, minimum size, maximum size, and geometry of the window according
        to the specified styles. Finally, it packs the main frame into the window.

        :param title: The title to set for the application window. If None, uses the
                      stored title.
        :type title: str or None
        """
        if title is None:
            title = self.title
        self.root.title = title
        self.root.configure(background=self.style['background'])
        self.root.minsize(*self.style['minsize'])
        self.root.maxsize(*self.style['maxsize'])
        self.root.geometry(self.style['geometry'])
        self.main_frame.pack()


    def loadView(self, view: View):
        """
        Loads a new view into the main application frame, replacing any existing widgets.

        :param view: The new view to be loaded, which must implement a `buildView` method that takes the main
                     application frame as a parameter.
        :type view: View

        :return: None
        """
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.root.update()
        view.buildView(self.main_frame)
        self.root.update()
        if not self.running:
            self.root.mainloop()
            self.running = True
        #self.main_frame.update()
        #self.root.mainloop()

class MainWindow(Window):
    """
    MainWindow class serves as the primary interface window for the application.

    :ivar title: The title of the main window.
    :type title: str
    """
    title = "MainWindow"