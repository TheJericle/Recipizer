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

class AddIngredient(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent)

        self.frame = tk.Frame(parent)

        ###Define the labels in the top left Corner
        self.label_ing_name = tk.Label(self.frame, text = "Ingredient Name :")
        self.label_quantity = tk.Label(self.frame, text = "Quantity :")
        self.label_unit = tk.Label(self.frame, text = "Unit :")

        ###Define the entry spaces matching the labels
        self.entry_ing_name = tk.Entry(self.frame)
        self.entry_quantity = tk.Entry(self.frame)
        self.entry_unit = tk.Entry(self.frame)

        ###Define the button, which will extract the given info and save the new ingredient.
        self.add_ingredient_button = tk.Button(self.frame, text="Add Ingredient")

    def setIngredientLabel(self, ing_name):
        self.entry_ing_name.delete(0, 'end')
        self.entry_ing_name.insert(0,ing_name)

    def setQuantityLabel(self, quantity):
        self.entry_quantity.delete(0, 'end')
        self.entry_quantity.insert(0,quantity)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

        self.label_ing_name.grid(column = 0, row = 0, sticky = tk.W)
        self.label_quantity.grid(column=0, row=1, sticky=tk.W)
        self.label_unit.grid(column=0, row=2, sticky=tk.W)

        self.entry_ing_name.grid(column=1, row=0, sticky=tk.W)
        self.entry_quantity.grid(column=1, row=1, sticky=tk.W)
        self.entry_unit.grid(column=1, row=2, sticky=tk.W)

        self.add_ingredient_button.grid(column=2, row=0, rowspan=3)

    def pack(self, **kwargs):
        print("not implemented yet...")




