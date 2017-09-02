#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from _future_ import absolute_import, division, print_function

# Import external modules
from Tkinter import *

# -----------------------------------------------------------------

def Store_Ingredient(event = None):
    ingredient = user_entry.get()
    Ingredient_List.append(ingredient)

def Print_Ingredients(event = None):
    for ing in Ingredient_List:
        print ing

# -----------------------------------------------------------------

root = Tk()

frame1 = Frame(root)
frame1.pack()

button_add_ingredient = Button(frame1, text = "add ingredient")
button_add_ingredient.pack()

Ingredient_List = []
user_entry = Entry(frame1)
user_entry.pack()

button_print_ingredients = Button(frame1, text = "print ingredients")
button_print_ingredients.pack()

button_print_ingredients.bind("<Button-1>",Print_Ingredients)
button_add_ingredient.bind("<Button-1>",Store_Ingredient)

root.mainloop()

# -----------------------------------------------------------------
