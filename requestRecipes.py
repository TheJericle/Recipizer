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

from gui.quantityScroll import quantityScroll
from gui.text_with_two_buttons_widget import TextTwoButtons

from core.Shopping_List_Class import ShoppingList
from core.Recipe_Class import Recipe
from core.Recipe_Book_Class import RecipeBook

class RequestRecipes(tk.Frame):
    """
    This window allows to user to set all his favored conditions and finally request a number of recipes.
    A shopping list is provided to the user, which he can accept or decline.

    This class thus contains the widgets necessary for this and an instance of the class RecipeBook
    This instance is provided by "recipe_book" in the creation of the widget.

    """
    def __init__(self, parent, recipe_book, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.recipe_book = recipe_book
        self.frame = tk.Frame(parent)

        self.Veggie_CheckButton = tk.Checkbutton(self.frame, text="Vegetarian")
        self.Vegan_CheckButton = tk.Checkbutton(self.frame, text="Vegan")

        self.NoPeople_Label = tk.Label(self.frame, text = "How many people?")
        self.NoPeople = quantityScroll(self.frame, range=(0,20))

        self.NoRecipes_Label = tk.Label(self.frame, text="How many Recipes?")
        self.NoRecipes = quantityScroll(self.frame, range=(0,20))

        self.receive_shopping_list_b = tk.Button(self.frame, text="Retreive Shopping List")

        self.receive_shopping_list_b.bind("<Button-1>", self.show_recipe_list)


    def grid(self, **kwargs):
        """
        Function places all the different widgets in the correct locations using the grid manager.

        :param kwargs: may contain any number of arguments(see tkinter grid documentation)

        """
        self.frame.pack()
        self.Veggie_CheckButton.grid(row=0, column=0,sticky=tk.SW)
        self.Vegan_CheckButton.grid(row=1, column=0,sticky=tk.SW)
        self.NoPeople_Label.grid(row=2, column=0)
        self.NoPeople.grid(row=3, column=0)
        self.NoRecipes_Label.grid(row=4, column=0)
        self.NoRecipes.grid(row=5, column=0)
        self.receive_shopping_list_b.grid(row=2, column=1, sticky=tk.N, padx=15)

    def show_recipe_list(self, event=None):
        """
        A window is popped up, showing the list of recipes. THe user can then reject or accept this list.
        Two bindings are created in this function:

        :Button1 binding:   If selected, the user has accepted the recipe list and should eventually
                            receive a shopping list

        :Button2 binding:   If selected, the user has rejected the recipe list and this function will be called
                            recursively.

        :param event:   the event that triggered the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """

        no_recipes = self.NoRecipes.hscale.get()

        self.recipe_list = self.recipe_book.get_recipes(no_recipes=no_recipes)

        self.recipe_list_widget_parent = tk.Toplevel()
        self.recipe_list_widget = TextTwoButtons(self.recipe_list_widget_parent)
        self.recipe_list_widget.grid()
        self.recipe_list_widget.set_name_button1("Satisfied")
        self.recipe_list_widget.set_name_button2("Try again")

        self.recipe_list_widget.Button1.bind("<Button-1>", self.button1press)
        self.recipe_list_widget.Button2.bind("<Button-1>", self.button2press)

        self.recipe_list_widget.textWindow.config(width=40, height=len(self.recipe_list))

        for rp in self.recipe_list:
            self.recipe_list_widget.textWindow.insert(tk.END, rp.name + "\n")

    def button1press(self, event=None):
        self.recipe_list_widget_parent.destroy()
        self.show_shopping_list()

    def button2press(self, event=None):
        self.recipe_list_widget_parent.destroy()
        self.show_recipe_list(event)

    def show_shopping_list(self):

        no_people = self.NoPeople.hscale.get()
        self.shopping_list_widget_parent = tk.Toplevel()
        self.shopping_list_widget = TextTwoButtons(self.shopping_list_widget_parent)

        self.shopping_list_widget.grid()
        self.shopping_list_widget.set_name_button1("Satisfied")
        self.shopping_list_widget.set_name_button2("Extra Satisfied")

        self.shopping_list_widget.Button1.bind("<Button-1>", self.button1press_n)
        self.shopping_list_widget.Button2.bind("<Button-1>", self.button2press_n)

        shopping_list = ShoppingList()
        for rp in self.recipe_list:
            for ing in rp._Ingredients:
                shopping_list.append(ing)

        self.shopping_list_widget.textWindow.config(width=40, height = len(shopping_list))

        for ing in shopping_list:
            ing*=no_people
            self.shopping_list_widget.textWindow.insert(tk.END, ing.inverse_parser() + "\n")
        self.shopping_list_widget.textWindow.insert(tk.END, "trala")

    def button1press_n(self, event=None):
        self.shopping_list_widget_parent.destroy()
        self.parent.destroy()

    def button2press_n(self, event=None):
        self.shopping_list_widget_parent.destroy()
        self.parent.destroy()



