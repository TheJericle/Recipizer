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

class TextAndButtonsWidget(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)

        self.textWindow = tk.Text(self.frame)

    def set_no_buttons(self, value):
        for i in range(value):

    def grid(self, **kwargs):
        self.frame.grid()
        self.textWindow.grid(column=0, row=0, columnspan = self.noButtons)