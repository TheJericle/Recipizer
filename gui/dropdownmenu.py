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
        self.frame.pack(**kwargs)

        self.vsb = tk.Scrollbar(self.frame)
        self.myList = tk.Listbox(self.frame, yscrollcommand = self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.myList.pack(side="left", fill="both", expand=True)


        self.vsb.config(orient="vertical", command=self.myList.yview)
        self.getlist()


    ###THIS NEEDS TO GETS FIXED, SO THAT IT WILL ALWAYS FIND THE RIGHT LOCATION FOR THE INGREDIENT FILE
    def getlist(self):
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "r")
        for line in f:
            self.myList.insert(tk.END, line)


    def addIngredientToList(self,ing_name, quantity, unit):
        self.myList.insert(tk.END, ing_name)
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "a")
        f.write(ing_name)