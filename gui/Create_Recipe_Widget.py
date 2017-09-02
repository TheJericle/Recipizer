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

# Import Recipizer modules
from .Add_Ingredient_Widget import AddIngredientWidget
from .DropDownMenu_Widget import DropDownMenu

# -----------------------------------------------------------------

class CreateRecipeWidget(object):

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.addIngredientWidget = AddIngredientWidget(self.frame)
        self.Known_Ingredients = DropDownMenu(self.frame)


# -----------------------------------------------------------------


root = Tk()

CreateRecipeWidget(root)

root.mainloop()

# -----------------------------------------------------------------
