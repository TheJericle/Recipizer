#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from _future_ import absolute_import, division, print_function

# Import external modules
import os

# Import Recipizer modules
from .Ingredient_Class import Ingredient
#from Recipe_Book_Class import RecipeBook

# -----------------------------------------------------------------

class ShoppingList(object):

    def __init__(self):
        self._Ingredient_List = []

    def append(self, ing):
        if not isinstance(ing, Ingredient):
            raise TypeError("Only ingredients can be added to the shoppinglist")
        else:
            if not self.check_if_present(ing):
                self._Ingredient_List.append(ing)
            else:
                index = self.find_ingredient(ing)
                self._Ingredient_List[index].quantity += ing.quantity

    def find_ingredient(self, new_ing):
        index = -1
        i = 0
        for ing in self._Ingredient_List:
            if ing == new_ing:
                index = i
                break
            i += 1
        return index

    def check_if_present(self, new_ing):
        out = False
        for ing in self._Ingredient_List:
            if ing == new_ing:
                out = True
                break
        return out

    def parser(self):
        cdir = os.getcwd()
        fileloc = os.path.join(cdir,"shoppinglist.txt")

        f = open(fileloc,'w')

        for ing in self._Ingredient_List:
            f.write(ing.inverse_parser())
            f.write("\n")

# -----------------------------------------------------------------
