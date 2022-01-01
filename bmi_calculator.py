#!/usr/bin/env python3

import tkinter
from tkinter import *

import lib.globals as config
from components.window import BaseWindow
from components.info import InfoWindow
from components.menu import MainMenu

config.init_globals()
config.set("FONT", "Arial")
config.set("FONT_SIZE", 18)
config.set("BG_COLOR", "blue")
config.set("THEME", "default")
config.set("WINDOW_WIDTH", 250)
config.set("WINDOW_HEIGHT", 150)
config.set("WINDOW_TITLE", "BMI Calculator")


## todo - change to self.root

class Application(Frame):
    """Main Application class"""

    def __init__(self, parent):
        '''Constructor'''
        Frame.__init__(self, parent=None)
        self.parent = parent
        self.pack()

        self.init_gui()

    def init_gui(self) -> None:
        '''Initializes GUI/Window'''
        BaseWindow.set_window_theme(self, config.get("THEME"))
        BaseWindow.set_window_attributes(
            self,
            config.get("WINDOW_TITLE"),
            config.get("BG_COLOR")
        )
        BaseWindow.set_window_size(
            self,
            width=config.get("WINDOW_WIDTH"),
            height=config.get("WINDOW_HEIGHT"),
            center=True
        )
        MainMenu(self.parent)

        # Widgets here
        self.name = Entry(self,
                          font=(
                              config.get('FONT'),
                              config.get('FONT_SIZE'), ""
                          ),
                          textvariable="entry"
                          )
        self.name.pack(side="top", fill="x")
        self.name.focus_set()

        choices = ['Meters/Kilograms',
                   'Centimeters/Kilograms',
                   'Inches/Pounds'
                   ]
        variable = StringVar(self)
        variable.set('Unit')
        w = OptionMenu(self, variable, *choices)
        w.pack()


        # Create Widgets
        btn = Button(self, text='Open Window', command=self.open_info_window)
        btn.pack(side="bottom")
        # Layout using grid
        #self.btn.grid(row=0, column=0, sticky='ew')

        # Layout stuff here

    def open_info_window(self):
        '''Calls info window'''
        self.new_window = tkinter.Toplevel(self.parent)
        InfoWindow(self.new_window)  # call new window class.


def main() -> None:
    root = Tk()
    root.resizable(width="false", height="false")

    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
