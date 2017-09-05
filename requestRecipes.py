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


class RequestRecipes(tk.Frame):
    """
    This window allows to user to set all his favored conditions and finally request a number of recipes.
    A shopping list is provided to the user, which he can accept or decline.

    This class thus contains the widgets necessary for this and an instance of the class RecipeBook
    This instance is provided by "recipe_book" in the creation of the widget.

    """
    def __init__(self, parent, recipe_book, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.recipe_book = recipe_book
        self.frame = tk.Frame(parent)

        self.Veggie_CheckButton = tk.Checkbutton(self.frame, text="Vegetarian")
        self.Vegan_CheckButton = tk.Checkbutton(self.frame, text="Vegan")

        self.NoPeople_Label = tk.Label(self.frame, text = "How many people?")
        self.NoPeople = quantityScroll(self.frame, range=(0,20))

        self.NoRecipes_Label = tk.Label(self.frame, text="How many Recipes?")
        self.NoRecipes = quantityScroll(self.frame, range=(0,100))

        self.receive_shopping_list_b = tk.Button(self.frame, text="Retreive Shopping List")

        self.receive_shopping_list_b.bind("<Button-1>", self.receive_shopping_list)


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

    def receive_shopping_list(self, event=None):
        """
        Retrieves a shopping list for the user. It starts by observing the required settings and then
        tries to find the requested number of recipies.

        These Recipes are then shown to the user, if he/she accepts it, a shopping list is provided.


        :param event:   the event that triggered the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """

        no_people = self.NoPeople.hscale.get()
        no_recipes = self.NoRecipes.hscale.get()

        recipe_list = self.recipe_book.get_recipes(no_recipes=no_recipes)

        self.text_with_two_buttons_widget_parent = tk.Toplevel()
        self.text_with_two_buttons_widget = TextTwoButtons(self.text_with_two_buttons_widget_parent)
        self.text_with_two_buttons_widget.grid()
        self.text_with_two_buttons_widget.set_name_button1("Satisfied")
        self.text_with_two_buttons_widget.set_name_button2("Try again")

        self.text_with_two_buttons_widget.Button1.bind("<Button-1>", self.button1press)
        self.text_with_two_buttons_widget.Button2.bind("<Button-2>", self.button2press)

        self.text_with_two_buttons_widget.textWindow.config(width=40, height=len(recipe_list))

        for rp in recipe_list:
            self.text_with_two_buttons_widget.textWindow.insert(tk.END, rp.name+"\n")



        #shopping_list = self.recipe_book.request_shopping_list(number_of_recipes=no_recipes, number_of_people=no_people)
        #text_shopping_list = shopping_list.parser()

    def button1press(self, event=None):
        self.text_with_two_buttons_widget_parent.destroy()

    def button2press(self, event=None):
        self.text_with_two_buttons_widget_parent.destroy()



