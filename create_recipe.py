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
from gui.add_ingredient import AddIngredient
from gui.dropdownmenu import dropdrownmenu
from gui.quantityScroll import quantityScroll
from gui.addRecipeRules import addRecipeRules

from core.Recipe_Class import Recipe
from core.Ingredient_Class import Ingredient
# -----------------------------------------------------------------


class Createrecipe(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.frame = tk.Frame(parent)

        #Add Ingredient Widget
        self.addIngredientWidget = AddIngredient(self.frame)

        #Available Ingredients Widget
        self.dropDownMenuLabel = tk.Label(self.frame, text="Available Ingredients:")
        self.dropDownMenuWidget = dropdrownmenu(self.frame)

        #Quantity SCroll widget
        self.quantityLabel = tk.Label(self.frame, text="Quantity: ")
        self.quantityScroll1 = quantityScroll(self.frame, range=(0,1000))

        #Shopping_List widget
        self.ingredientLabel = tk.Label(self.frame, text="Shopping List:")
        self.ingredientTextBox = tk.Text(self.frame, width=40, height=1)

        #RecipeRuleWidget
        self.explainText = addRecipeRules(self.frame)

        #Add Recipe Button
        self.addRecipeButton = tk.Button(self.frame, text="Submit Recipe")


        #Event Bindings
        self.dropDownMenuWidget.myList.bind("<Double-Button-1>", self.get_currently_selected_ingredient)
        self.addIngredientWidget.add_ingredient_button.bind("<Button-1>", self.extract_ingredient)
        self.quantityScroll1.hscale.bind("<ButtonRelease-1>", self.get_currently_selected_quantity)





    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
        self.addIngredientWidget.grid(column=0, row=0, pady=15)
        self.dropDownMenuLabel.grid(row=1, column=0)
        self.dropDownMenuWidget.grid(column=0, row=2, pady=15)
        self.quantityLabel.grid(row=1, column=1)
        self.quantityScroll1.grid(row=2, column=1)
        self.ingredientLabel.grid(row=3, column=0, pady=5)
        self.ingredientTextBox.grid(row=4, column=0)
        self.explainText.grid(row=0, column=2, padx=20, pady=50)
        self.addRecipeButton.grid(row=2, column=2)

    def get_currently_selected_ingredient(self, event=None):
        currentlyselected = self.dropDownMenuWidget.myList.get(tk.ACTIVE)
        self.addIngredientWidget.setIngredientLabel(currentlyselected)

    def get_currently_selected_quantity(self, event=None):
        currentlyselected = self.quantityScroll1.hscale.get()
        self.addIngredientWidget.setQuantityLabel(currentlyselected)

    def extract_ingredient(self, event=None):
        ing_name = self.addIngredientWidget.entry_ing_name.get()
        quantity = self.addIngredientWidget.entry_quantity.get()
        unit = self.addIngredientWidget.entry_unit.get()

        ingredient_currently_present = False

        for known_ing in self.dropDownMenuWidget.myList.get(0, tk.END):
            if known_ing==ing_name:
                ingredient_currently_present = True

        if not ingredient_currently_present:
            self.dropDownMenuWidget.addIngredientToList(ing_name, quantity, unit)

        self.add_ingredient_to_textbox(ing_name, quantity, unit)

    def add_ingredient_to_textbox(self, ing_name, quantity, unit):
        ing_name = ing_name.split("\n")[0]
        self.ingredientTextBox.insert(tk.END, ing_name+"\t"+quantity+"\t"+unit+"\n")
        cheight = self.ingredientTextBox.cget("height")
        self.ingredientTextBox.config(height=int(cheight)+1)

    def add_recipe(self, event=None):
        ingredient_List = self.retreive_shoppingList()
        recipe_List = self.retreive_recipeList()

        newRecipe = Recipe()
        for ing in ingredient_List:
            ing = ing.split("\t")
            newIngredient = Ingredient()
            newIngredient.name = str(ing[0])
            newIngredient.quantity = float(ing[1])
            newIngredient.unit = str(ing[2])
            newRecipe.append(newIngredient)

        #print(recipe_List)
        for rule in recipe_List:
            newRecipe.append(str(rule))
        print("GET DESTROYED")
        self.parent.destroy()

    def retreive_shoppingList(self):

        ingredient_List = []
        ingredient_input = self.ingredientTextBox.get(1.0, tk.END)
        ingredient_input = ingredient_input.split("\n")


        for item in ingredient_input:
            if item == "":
                continue
            ingredient_List.append(item)
        return ingredient_List

    def retreive_recipeList(self):

        recipeRule_List = []
        recipe_input = self.explainText.get(1.0, tk.END)
        recipe_input = recipe_input.split("\n")

        for item in recipe_input:
            if item == "":
                continue
            recipeRule_List.append(item)

        return recipeRule_List




