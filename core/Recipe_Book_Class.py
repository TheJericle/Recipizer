#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

# Import external modules
import random
import os

# Import Recipizer modules
from .Recipe_Class import Recipe
from .Shopping_List_Class import ShoppingList

# -----------------------------------------------------------------

class RecipeBook(object):

    def __init__(self):
        self._Recipe_List = []

    def append(self, rp):
        if isinstance(rp, Recipe):
            self._Recipe_List.append(rp)
        else:
            raise TypeError("Only REcipes can be added to the RecipeBook")

    def __len__(self):
        return len(self._Recipe_List)

    def __getitem__(self, index):
        return self._Recipe_List[index]

    def __delitem__(self, key):
        del self._Recipe_List[key]

    def insert(self, index, rp):
        self._Recipe_List.insert(index, rp)

    def get_random_recipe(self):
        rv = random.randint(0, len(self._Recipe_List)-1)
        return self._Recipe_List[rv]

    def get_recipes(self, no_recipes):
        if len(self)<no_recipes:
            raise LookupError("There are not enough recipes in the RecipeBook...")

        rp_list = []
        index = 0
        while index <no_recipes:
            new_recipe = self.get_random_recipe()
            if new_recipe in rp_list:
                continue
            else:
                rp_list.append(new_recipe)
            index+=1
        return rp_list

    def make_shopping_list(self, rp_list):

        new_shopping_list = ShoppingList()
        new_shopping_list.get_ingredients_from_rp_list(rp_list)

        return new_shopping_list

    def inverse_parser(self):
        output = []
        for i in range(0, len(self._Recipe_List)):
            output = output + self._Recipe_List[i].inverse_parser()
        return output

    def read_file(self, filename):
        cdir = os.getcwd()
        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "r")

        output = []
        for line in f:
            line = line.split()
            output.append(line)
        return output

    def split_into_recipes(self, file_output):
        recipe_list = []
        recipe = []
        for line in file_output:

            if line[0] == "Start_Recipe:":
                if len(recipe)!=0:
                    temp_list = recipe[:]
                    recipe_list += [temp_list]
                del recipe[:]
                recipe.append(line)
            else:
                recipe.append(line)
        recipe_list+=[recipe]
        return recipe_list

    def parser(self, filename):
        file_output = self.read_file(filename)
        recipe_list = self.split_into_recipes(file_output)
        for rp in recipe_list:
            new_recipe = Recipe()
            new_recipe.parser(rp)
            self.append(new_recipe)

    def update_recipe_book(self):
        cdir = os.getcwd()
        fileloc = os.path.join(cdir, "Recipe_Book.txt")

        f = open(fileloc, "w")

        output = self.inverse_parser()

        for line in output:
            f.write(line+"\n")


# -----------------------------------------------------------------
