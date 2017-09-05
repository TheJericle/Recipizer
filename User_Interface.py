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
import os
from PIL import Image, ImageTk

# Import Recipizer modules
from create_recipe import Createrecipe
from requestRecipes import RequestRecipes

from core.Recipe_Class import Recipe
from core.Recipe_Book_Class import RecipeBook# -----------------------------------------------------------------



class UserInterface(tk.Frame):
    """This is the main userinterface, which will redirect the user.
       Currently there are two options:
       -Create a Recipe (accesed through the "Create New Recipe" button)
       -Request a shoppinglist( access through the "Request Recipes" button)

       This class thus contains the widgets necessary for this and an instance of the class
       RecipeBook, which contains all the currently documented recipes.

    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent)

        self.frame = tk.Frame(parent)


        self.add_recipe_b = tk.Button(self.frame, text="Create New Recipe")
        self.add_recipe_b.grid(column=0, row=0, padx=20, pady=20)

        self.request_recipes_b = tk.Button(self.frame, text= "Request Recipes")


        self.photo_container = tk.Label()
        self.set_photo(filename="What_Is_My_Purpose.jpg")


        self.add_recipe_b.bind("<Button-1>", self.add_recipes)
        self.request_recipes_b.bind("<Button-1>", self.request_recipes)

        self.recipe_book = RecipeBook()
        self.recipe_book.parser("Recipe_Book.txt")

    def grid(self, **kwargs):
        """
        Function places all the different widgets in the correct locations using the grid manager.

        :param kwargs: may contain any number of arguments(see tkinter grid documentation)
        """

        self.frame.grid()
        self.request_recipes_b.grid(column=1, row=0)
        self.photo_container.grid(column=0, row=1)

    #THIS NEEDS TO BE ADJUSTED SO IT WILL ALWAYS WORKS(I.E, the correct fileloc is extracted)
    def set_photo(self, filename):
        """Functions simply sets an image at the GUI

        :param filename: location of the image
        """
        cdir = os.getcwd()
        filename = os.path.join("images\\", filename)
        fileloc = os.path.join(cdir, filename)
        image = Image.open(fileloc)
        image.thumbnail((350, 350), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.photo_container.config(image=photo)
        self.photo_container.image = photo  # keep a reference!

    def add_recipes(self, event=None):
        """
        Functions pops up a window which allows to user to submit all the details to a new recipe.
        A new image is set after this function is called.

        A new binding is created for the submit_recipe button in the new window

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """

        self.set_photo(filename="Szechuan_Sauce.jpg")
        self.createRecipeWindow = Createrecipe(parent=tk.Toplevel())
        self.createRecipeWindow.grid()

        #self.createRecipeWindow.addRecipeButton.bind("<Button-1>", self.createRecipeWindow.add_recipe)
        self.createRecipeWindow.addRecipeButton.bind("<Button-1>",self.submit_recipe)


    def request_recipes(self,event=None):
        """
        Functions pops up a new window which allow the user to request a number of recipes

        A new image is set after this function is called.

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.

        """
        self.set_photo(filename="caaan_do.jpg")
        self.RequestRecipesWindow = RequestRecipes(parent=tk.Toplevel(),recipe_book=self.recipe_book)
        self.RequestRecipesWindow.grid()

    #A recipe has been submitted, a new window pops up, asking the user if this is what he wants.
    #The recipe then needs to be extracted from self.createRecipeWindow
    def submit_recipe(self, event=None):
        """
        This function is called when the user is submitting the recipe.
        The new recipe instance is extraced from the Createrecipe widget and added to
        the recipe book instance.

        All redundant window are closed.

        :param event:   the event that triggerd the call to this function, is required to be a parameter of
                        the function(see tkinter documentation), but is not required here.
        """
        self.createRecipeWindow.add_recipe(event=None)

        new_recipe = self.createRecipeWindow.new_recipe

        self.recipe_book.append(new_recipe)
        self.recipe_book.update_recipe_book()

root = tk.Tk()

test = UserInterface(root)
test.grid()

root.mainloop()
