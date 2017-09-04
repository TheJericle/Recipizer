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

# -----------------------------------------------------------------

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent)

        self.frame = tk.Frame(parent)
        self.frame.grid()

        self.add_recipe_b = tk.Button(self.frame, text="Create New Recipe")
        self.add_recipe_b.grid(column=0, row=0, padx=20, pady=20)

        self.request_recipes_b = tk.Button(self.frame, text= "Request Recipes")
        self.request_recipes_b.grid(column=1, row=0)

        self.photo_container = tk.Label()
        self.set_photo(filename="What_Is_My_Purpose.jpg")
        self.photo_container.grid(column=0, row=1)

        self.add_recipe_b.bind("<Button-1>", self.add_recipes)
        self.request_recipes_b.bind("<Button-1>", self.request_recipes)


    ###THIS NEEDS TO BE ADJUSTED SO IT WILL ALWAYS WORKS
    def set_photo(self, filename):
        cdir = os.getcwd()
        filename = os.path.join("images\\", filename)
        fileloc = os.path.join(cdir, filename)
        image = Image.open(fileloc)
        image.thumbnail((350, 350), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.photo_container.config(image=photo)
        self.photo_container.image = photo  # keep a reference!

    def add_recipes(self, event=None):

        self.set_photo(filename="Szechuan_Sauce.jpg")
        self.createRecipeWindow = Createrecipe(tk.Toplevel())
        self.createRecipeWindow.grid()

        self.createRecipeWindow.addRecipeButton.bind("<Button-1>", self.createRecipeWindow.add_recipe)

    def request_recipes(self,event=None):

        self.set_photo(filename="caaan_do.jpg")
        self.RequestRecipesWindow = RequestRecipes(tk.Toplevel())
        self.RequestRecipesWindow.grid()


root = tk.Tk()

UserInterface(root)

root.mainloop()
