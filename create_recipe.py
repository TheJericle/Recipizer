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
from gui.add_ingredient import add_ingredient
from gui.dropdownmenu import dropdrownmenu

# -----------------------------------------------------------------

class createrecipe(tk.Frame):

    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.addIngredientWidget = add_ingredient(self.frame)
        self.dropDownMenuLabel = tk.Label(self.frame, text ="Available Ingredients:")
        self.dropDownMenuLabel.pack(side=tk.LEFT, fill = tk.Y)
        self.dropDownMenuWidget = dropdrownmenu(self.frame)

        self.dropDownMenuWidget.bind("<Double-Button-1>", self.get_currently_selected_ingredient)
        #self.currentlySelected = tk.StringVar()
        #self.currentlySelected = self.dropDownMenuWidget.myList.get(tk.ACTIVE)


    def get_currently_selected_ingredient(self, event=None):
        print("this is happening")
        #self.currentlySelected = self.dropDownMenuWidget.currentlySelected
        #self.addIngredientWidget.setIngredientLabel(self.currentlySelected)


root = tk.Tk()

test = createrecipe(root)


root.mainloop()