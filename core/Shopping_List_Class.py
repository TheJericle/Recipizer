#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

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

    def __getitem__(self, index):
        return self._Ingredient_List[index]

    def __len__(self):
        return len(self._Ingredient_List)

    def __iter__(self):
        self.index = 0
        return self

    def next(self):
        if self.index < len(self):
            out = self[self.index]
            self.index+=1
            return out
        else:
            raise StopIteration

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

    def get_ingredients_from_rp_list(self, rp_list):
        for rp in rp_list:
            for ing in rp._Ingredients:
                self.append(ing)


    def parser(self):
        cdir = os.getcwd()
        fileloc = os.path.join(cdir,"shoppinglist.txt")

        f = open(fileloc,'w')

        for ing in self._Ingredient_List:
            f.write(ing.inverse_parser())
            f.write("\n")

# -----------------------------------------------------------------

