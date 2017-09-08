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
from gui.text_with_two_buttons_widget import TextTwoButtons


from core.Recipe_Class import Recipe
from core.Ingredient_Class import Ingredient
# -----------------------------------------------------------------


class Createrecipe(tk.Frame):
    """
    This widget creates a window containing everything the user needs to submit a new recipe

    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.frame = tk.Frame(parent)

        #Add Recipe_Name_Box:
        self.recipe_name_label = tk.Label(self.frame, text= "Recipe Name:")
        self.recipe_name_entry = tk.Entry(self.frame)


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


        self.new_recipe = Recipe()




    def grid(self, **kwargs):
        """
          Function places all the different widgets in the correct locations using the grid manager.

          :param kwargs: may contain any number of arguments(see tkinter grid documentation)
          """
        self.frame.grid(**kwargs)
        self.recipe_name_label.grid(column=1,row=0,pady=10)
        self.recipe_name_entry.grid(column=2,row=0)
        self.addIngredientWidget.grid(column=0, row=1, pady=10)
        self.dropDownMenuLabel.grid(row=2, column=0)
        self.dropDownMenuWidget.grid(column=0, row=3, pady=10)
        self.quantityLabel.grid(row=2, column=1)
        self.quantityScroll1.grid(row=3, column=1)
        self.ingredientLabel.grid(row=4, column=0, pady=5)
        self.ingredientTextBox.grid(row=5, column=0)
        self.explainText.grid(row=1, column=2, padx=20, pady=40)
        self.addRecipeButton.grid(row=3, column=2)

    def get_currently_selected_ingredient(self, event=None):
        """
        Function detects the currently selected ingredient from the dropdownmenu and sets it as
        the current ingredient

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """
        currentlyselected = self.dropDownMenuWidget.myList.get(tk.ACTIVE)
        self.addIngredientWidget.setIngredientLabel(currentlyselected)

    def get_currently_selected_quantity(self, event=None):
        """
        Function detects the currently selected quantity from the quantity scroller and sets it as
        the current quantity

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """
        currentlyselected = self.quantityScroll1.hscale.get()
        self.addIngredientWidget.setQuantityLabel(currentlyselected)

    def extract_ingredient(self, event=None):
        """
        This function is called when the "add new ingredient" button is selected. It extracts all the relevant information
        and stores it in the designated textbox.
        It also checks if the ingredient is already present in the list of possible ingredienst, if not this name will
        be added to the list.

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """
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
        """
        This function adds all the ingredient information to the designated textbox.

        :param ing_name: Name of the ingredient
        :param quantity: quantity of the ingredient
        :param unit: unit of the ingredient

        """
        ing_name = ing_name.split("\n")[0]
        self.ingredientTextBox.insert(tk.END, ing_name+"\t"+quantity+"\t"+unit+"\n")
        cheight = self.ingredientTextBox.cget("height")
        self.ingredientTextBox.config(height=int(cheight)+1)


    def add_recipe(self, event=None):
        """
        This functions prepares everything to add a recipe to self.RecipeBook.

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """

        #Relevant Recipe Info is extracted.
        ingredient_List = self.retreive_shoppingList()
        recipe_List = self.retreive_recipeList()
        recipe_name = self.retreive_recipe_name()

        #Recipe name is added to the recipe.
        self.new_recipe.name = recipe_name

        #Ingredients are added to the recipe.
        for ing in ingredient_List:
            ing = ing.split("\t")
            newIngredient = Ingredient()
            newIngredient.name = str(ing[0])
            newIngredient.quantity = float(ing[1])
            newIngredient.unit = str(ing[2])
            self.new_recipe.append(newIngredient)

        #Recipe rules are added.
        for rule in recipe_List:
            self.new_recipe.append(str(rule))

        #A window pops up, asking the user if the current recipe template looks fine.
        self.create_recipe_template_window()

        template_list = self.new_recipe.inverse_parser()
        self.template_window.textWindow.config(width=40, height=len(template_list))


        for i in range(0,len(template_list)):
            self.template_window.textWindow.insert(tk.END, template_list[i] + "\n")


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

    def retreive_recipe_name(self):
        return self.recipe_name_entry.get()


    def create_recipe_template_window(self):

        self.template_window_parent = tk.Toplevel()
        self.template_window = TextTwoButtons(self.template_window_parent)
        self.template_window.grid()
        self.template_window.set_name_button1("Satisfactionary")
        self.template_window.set_name_button2("Get This Shit OUTA MY FACE")
        
        

        self.template_window.Button1.bind("<Button-1>", self.button1press)
        self.template_window.Button2.bind("<Button-1>", self.button2press)


    def button1press(self, event=None):
        self.parent.destroy()
        self.template_window_parent.destroy()


    def button2press(self, event=None):
        self.template_window_parent.destroy()






