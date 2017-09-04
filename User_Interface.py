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

# -----------------------------------------------------------------

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent)

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.add_recipe_b = tk.Button(self.frame, text="Create New Recipe")
        self.add_recipe_b.grid(column=0, row=0, padx=20, pady=20)

        self.request_recipes_b = tk.Button(self.frame, text= "Request Recipes")
        self.request_recipes_b.grid(column=1, row=0)


        self.add_recipe_b.bind("<Button-1>", self.add_recipes)
        self.request_recipes_b.bind("<Button-1>", self.request_recipes)

    def add_recipes(self, event=None):

        self.createRecipeWindow = Createrecipe(tk.Toplevel())
        self.createRecipeWindow.grid()

        self.createRecipeWindow.addRecipeButton.bind("<Button-1>", self.createRecipeWindow.add_recipe)

    def request_recipes(self,event=None):

        cdir = os.getcwd()
        filename = "1727338_1.jpg"
        fileloc = os.path.join(cdir,filename)
        image = Image.open(fileloc)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.image = photo # keep a reference!
        label.pack()
        return None

root = tk.Tk()

UserInterface(root)

root.mainloop()
