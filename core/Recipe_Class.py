#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

# Import Recipizer modules
from .Ingredient_Class import Ingredient

# -----------------------------------------------------------------

class Recipe(object):

    def __init__(self):
        self._name = ""
        self._Ingredients = []
        self._Basic_Explanation = []

    def __iter__(self):
        return iter(self._Ingredients)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Please provide a string for the name of the Recipe")
        else:
            self._name = value

    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return False
        else:
            if self.name !=other.name:
                return False
            if len(self._Basic_Explanation) != len(other._Basic_Explanation):
                return False
            if len(self._Ingredients) != len(other._Ingredients):
                return False
            for ing1,ing2 in zip(self._Ingredients,other._Ingredients):
                if ing1!=ing2:
                    return False

            for exp1,exp2 in zip(self._Basic_Explanation,other._Basic_Explanation):
                if exp1!=exp2:
                    return False

        return True

    def append(self, thingie):
        if isinstance(thingie, Ingredient):
            self._Ingredients.append(thingie)

        elif isinstance(thingie, str):
            self._Basic_Explanation.append(thingie)

        else:
            raise TypeError("Appending an object to the Recipe should either be an ingredient or a part of the "
                            "explanation (i.e. a string)")

    def inverse_parser(self):
        output = ["Start_Recipe:", "Recipe_Name=" + self.name, "Ingredients:"]

        for i in range(0, len(self._Ingredients)):
            output.append(self._Ingredients[i].inverse_parser())
        output.append("Basic_Explanation:")

        for i in range(0, len(self._Basic_Explanation)):
            output.append(self._Basic_Explanation[i])
        output.append('End_Recipe:')

        return output

    def parser(self, new_recipe):
        if not (new_recipe[0] == ["Start_Recipe:"] and new_recipe[len(new_recipe)-1] == ["End_Recipe:"]):
            raise ImportError("somethings wrong with the filereader...")
        else:
            # removes the "Recipe_Name = " part of the string(i.e. extract the name)
            self.name = new_recipe[1][0][12:]

            index = 3
            line = new_recipe[3]
            while line[0] != "Basic_Explanation:":
                new_ingredient = Ingredient()
                new_ingredient.parser(line)
                self.append(new_ingredient)
                index += 1
                line = new_recipe[index]

            index+=1
            line= new_recipe[index]
            while line[0] != "End_Recipe:":
                self.append(line[0])
                index +=1
                line = new_recipe[index]

# -----------------------------------------------------------------
