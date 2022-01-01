#!/usr/bin/env python3

from tkinter import ttk

class BaseWindow():
    """Base Window methods"""
    def set_window_size(self, width, height, center=True) -> None:
        '''Sets size and postion of window'''
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x, y = 0, 0

        if center:
            x = (screen_width - width) / 2
            y = (screen_height - height) / 2

        self.parent.geometry('%dx%d+%d+%d' % (
            width, height, x, y
        ))

    def set_window_theme(self, theme) -> None:
        '''Sets theme for window'''
        self.style = ttk.Style(self)
        self.style.theme_use(theme)

    def set_window_attributes(self, title, background_color) -> None:
        '''Sets attributes for window'''
        self.winfo_toplevel().title(title)
        self.parent.configure(bg=background_color)
