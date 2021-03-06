#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

import Tkinter as tk
import os


# -----------------------------------------------------------------

class dropdrownmenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)

        self.vsb = tk.Scrollbar(self.frame)
        self.myList = tk.Listbox(self.frame, yscrollcommand = self.vsb.set, width=20, height=4)

        self.vsb.config(orient="vertical", command=self.myList.yview)
        self.getlist()

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

        self.vsb.pack(side = "right", fill ="y")
        self.myList.pack(side="left", fill="both", expand=True)

    ###THIS NEEDS TO GETS FIXED, SO THAT IT WILL ALWAYS FIND THE RIGHT LOCATION FOR THE INGREDIENT FILE
    def getlist(self):
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "r")
        temp_list = []
        for line in f:
            line.split("\n")
            temp_list.append(line)
        temp_list.sort()

        for line in temp_list:
            self.myList.insert(tk.END, line)

    ###SAME HERE###
    def addIngredientToList(self,ing_name, quantity, unit):
        if self.check_if_ingredient_in_list(ing_name):
            return None

        self.myList.insert(tk.END, ing_name)
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "a")
        f.write(ing_name + "\n")

    def check_if_ingredient_in_list(self, ing_name):
        for ing in self.myList.get(0,tk.END):
            if ing == ing_name:
                return True
        return False

    #Returns the correct index for the ingredient to be added to the list
    #in such a way that the order stays alphabetically.
    def find_ingredient_index(self,ing_name):
        return None