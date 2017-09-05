#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

# Import external modules
import Tkinter as tk


class RecipeTemplate(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)

        self.textWindow = tk.Text(self.frame)
        self.Button1 = tk.Button(self.frame, text="Satisfactionary")
        self.Button2 = tk.Button(self.frame, text="Get This Shit OUTA MY FACE")


    def grid(self, **kwargs):
        self.frame.grid()
        self.textWindow.grid(column=0, row=0, columnspan = 2)
        self.Button1.grid(column=0, row=1, pady=20)
        self.Button2.grid(column=1, row=1)

    def insert(self, index, text):
        self.textWindow.insert(index, text)





