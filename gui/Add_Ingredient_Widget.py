#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

# Import external modules
from Tkinter import *

# -----------------------------------------------------------------

class AddIngredientWidget(object):

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.label_ing_name = Label(self.frame, text = "Ingredient Name :")
        self.label_quantity = Label(self.frame, text = "Quantity :")
        self.label_unit = Label(self.frame, text = "Unit :")

        self.label_ing_name.grid(column = 0, row = 0, sticky = W)
        self.label_quantity.grid(column=0, row=1, sticky=W)
        self.label_unit.grid(column=0, row=2, sticky=W)

        self.entry_ing_name = Entry(self.frame)
        self.entry_quantity = Entry(self.frame)
        self.entry_unit = Entry(self.frame)

        self.entry_ing_name.grid(column=1, row=0, sticky=W)
        self.entry_quantity.grid(column=1, row=1, sticky=W)
        self.entry_unit.grid(column=1, row=2, sticky=W)

        self.add_ingredient_button = Button(self.frame, text = "Add Ingredient")

        self.add_ingredient_button.grid(column = 2, row = 0, rowspan = 3)

        self.add_ingredient_button.bind("<Button-1>",self.add_ingredient)

    def add_ingredient(self,event =None):
        print (self.entry_ing_name.get())
        print (self.entry_quantity.get())
        print (self.entry_unit.get())

# -----------------------------------------------------------------
