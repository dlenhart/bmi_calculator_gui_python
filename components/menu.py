#!/usr/bin/env python3

import tkinter
from tkinter import messagebox, ttk

class MainMenu(ttk.Frame):
    """Main Menu Bar"""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.root = parent
        self.init_menubar()

    def exit(self) -> None:
        '''Exits the application'''
        quit()

    def about(self) -> None:
        pass

    def init_menubar(self) -> None:
        '''Initializes the menu bar'''
        self.menubar = tkinter.Menu(self.root)

        self.file = tkinter.Menu(self.menubar)
        self.file.add_command(label="About", command=self.about)
        self.file.add_command(label='Exit', command=self.exit)
        self.menubar.add_cascade(menu=self.file, label='File')

        self.root.config(menu=self.menubar)