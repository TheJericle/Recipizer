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
from gui.addRecipeRules import addRecipeRules
# -----------------------------------------------------------------

class createrecipe(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)
        self.frame.grid()

        self.addIngredientWidget = add_ingredient(self.frame, column = 0, row = 0, pady = 15)


        self.dropDownMenuLabel = tk.Label(self.frame, text ="Available Ingredients:")
        self.dropDownMenuLabel.grid(row =1,column =0)

        self.dropDownMenuWidget = dropdrownmenu(self.frame, column = 0, row = 2, pady = 15)
        self.dropDownMenuWidget.myList.bind("<Double-Button-1>", self.get_currently_selected_ingredient)


        self.quantityLabel = tk.Label(self.frame,text="Quantity: ")
        self.quantityLabel.grid(row =1, column = 1)
        self.quantityScroll1 = quantityScroll(self.frame, row = 2, column = 1)
        self.quantityScroll1.hscale.bind("<ButtonRelease-1>", self.get_currently_selected_quantity)

        self.ingredientLabel = tk.Label(self.frame, text = "Shopping List:")
        self.ingredientLabel.grid(row = 5, column=0,pady = 5)
        self.ingredientTextBox = tk.Text(self.frame, width=40, height=1)
        self.ingredientTextBox.grid(row = 6, column =0)

        self.explainText = addRecipeRules(self.frame,row = 0, column  = 6, padx = 20,pady = 50)

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

        self.add_ingredient_to_textbox(ing_name, quantity, unit)

    def add_ingredient_to_textbox(self, ing_name, quantity, unit):
        ing_name = ing_name.split("\n")[0]
        self.ingredientTextBox.insert(tk.END,ing_name +"\t" + quantity + "\t" + unit + "\n")
        cheight = self.ingredientTextBox.cget("height")
        self.ingredientTextBox.config(height = int(cheight)+1)

root = tk.Tk()

test = createrecipe(root)


root.mainloop()