#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function


import Tkinter as tk

class Foo(tk.Frame):
    """Foo example"""

    def __init__(self, master=None):
        """Draw Foo GUI"""
        tk.Frame.__init__(self, master)
        self.grid()
        self.draw_window_bar()

    def draw_window_bar(self):
        """Draw bar TopLevel window"""
        self.window_bar = tk.Toplevel(self)
        # Some uber-pythonian code here...
        ask_yes_or_no = tk.messagebox.askyesno('Brian?', 'Romani Ite Domum')
        if not ask_yes_or_no:
            self.window_bar.destroy()

root = tk.Tk()

Foo(root)

root.mainloop()