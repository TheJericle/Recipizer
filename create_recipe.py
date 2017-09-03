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

# Import Recipizer modules
from gui.add_ingredient import add_ingredient
from gui.dropdownmenu import dropdrownmenu
from gui.quantityScroll import quantityScroll
# -----------------------------------------------------------------

class createrecipe(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.addIngredientWidget = add_ingredient(self.frame, side=tk.TOP)


        self.dropDownMenuLabel = tk.Label(self.frame, text ="Available Ingredients:")
        self.dropDownMenuLabel.pack(side=tk.LEFT, fill = tk.Y)
        self.dropDownMenuWidget = dropdrownmenu(self.frame,side= tk.LEFT)
        self.dropDownMenuWidget.myList.bind("<Double-Button-1>", self.get_currently_selected_ingredient)


        self.quantityLabel = tk.Label(self.frame,text="Quantity: ")
        self.quantityLabel.pack(side=tk.LEFT, padx= 20)
        self.quantityScroll1 = quantityScroll(self.frame, side=tk.RIGHT)
        self.quantityScroll1.hscale.bind("<ButtonRelease-1>", self.get_currently_selected_quantity)

        self.addIngredientWidget.add_ingredient_button.bind("<Button-1>", self.extract_ingredient)




    def get_currently_selected_ingredient(self, event=None):

        currentlySelected = self.dropDownMenuWidget.myList.get(tk.ACTIVE)
        self.addIngredientWidget.setIngredientLabel(currentlySelected)

    def get_currently_selected_quantity(self, event=None):
        currentlySelected = self.quantityScroll1.hscale.get()
        self.addIngredientWidget.setQuantityLabel(currentlySelected)

    def extract_ingredient(self, event=None):
        ing_name = self.addIngredientWidget.entry_ing_name.get()
        quantity = self.addIngredientWidget.entry_quantity.get()
        unit = self.addIngredientWidget.entry_unit.get()

        ingredient_currently_present = False

        for known_ing in self.dropDownMenuWidget.myList.get(0,tk.END):
            if known_ing==ing_name:
                ingredient_currently_present = True

        if not ingredient_currently_present:
            self.dropDownMenuWidget.addIngredientToList(ing_name, quantity, unit)



root = tk.Tk()

test = createrecipe(root)


root.mainloop()