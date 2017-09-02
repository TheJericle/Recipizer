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

# -----------------------------------------------------------------

class add_ingredient(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent)

        self.frame = tk.Frame(parent)
        self.frame.pack()

        ###Define the labels in the top left Corner
        self.label_ing_name = tk.Label(self.frame, text = "Ingredient Name :")
        self.label_quantity = tk.Label(self.frame, text = "Quantity :")
        self.label_unit = tk.Label(self.frame, text = "Unit :")

        self.label_ing_name.grid(column = 0, row = 0, sticky = tk.W)
        self.label_quantity.grid(column=0, row=1, sticky=tk.W)
        self.label_unit.grid(column=0, row=2, sticky=tk.W)

        ###Define the entry spaces matching the labels
        self.entry_ing_name = tk.Entry(self.frame)
        self.entry_quantity = tk.Entry(self.frame)
        self.entry_unit = tk.Entry(self.frame)

        self.entry_ing_name.grid(column=1, row=0, sticky=tk.W)
        self.entry_quantity.grid(column=1, row=1, sticky=tk.W)
        self.entry_unit.grid(column=1, row=2, sticky=tk.W)

        ###Define the button, which will extract the given info and save the new ingredient.
        self.add_ingredient_button = tk.Button(self.frame, text="Add Ingredient")
        self.add_ingredient_button.grid(column=2, row=0, rowspan=3)
        self.add_ingredient_button.bind("<Button-1>", self.button_add_ingredient)

    def setIngredientLabel(self, ing_name):
        self.entry_ing_name.delete(0, 'end')
        self.entry_ing_name.insert(0,ing_name)


    def button_add_ingredient(self, event=None):
        print(self.entry_ing_name.get())
        print(self.entry_quantity.get())
        print(self.entry_unit.get())

