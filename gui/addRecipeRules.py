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


# -----------------------------------------------------------------

class addRecipeRules(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)

        self.label = tk.Label(self.frame, text = "Recipe rules")

        self.RecipeTextBox = tk.Text(self.frame, width = 40, height = 3)

        self.RecipeTextBox.bind("<Return>", self.recipeRuleAdded)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
        self.label.grid(column=0, row=0)
        self.RecipeTextBox.grid(column=0, row=1)

    def recipeRuleAdded(self, event=None):
        cheight = self.RecipeTextBox.cget("height")
        self.RecipeTextBox.config(height = cheight+1)

    def get(self,start,end):
        return self.RecipeTextBox.get(start,end)


