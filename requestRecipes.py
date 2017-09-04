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

class RequestRecipes(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

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

        self.frame.pack()
        self.Veggie_CheckButton.grid(row=0, column=0,sticky=tk.SW)
        self.Vegan_CheckButton.grid(row=1, column=0,sticky=tk.SW)
        self.NoPeople_Label.grid(row=2, column=0)
        self.NoPeople.grid(row=3, column=0)
        self.NoRecipes_Label.grid(row=4, column=0)
        self.NoRecipes.grid(row=5, column=0)
        self.receive_shopping_list_b.grid(row=2, column=1, sticky=tk.N, padx=15)

    def receive_shopping_list(self, event=None):

        #Start by collecting the required data
        no_people = self.NoPeople.hscale.get()
        no_recipes = self.NoRecipes.hscale.get()

