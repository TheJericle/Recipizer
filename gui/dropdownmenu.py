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
        self.frame.pack()

        self.vsb = tk.Scrollbar(self.frame)
        self.myList = tk.Listbox(self.frame, yscrollcommand = self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.myList.pack(side="left", fill="both", expand=True)


        self.vsb.config(orient="vertical", command=self.myList.yview)
        self.getlist()

        #self.myList.bind("<Double-Button-1>",self.get_clicked_value)
        #self.currentlySelected = tk.StringVar()
        #self.currentlySelected.set(self.myList.get(tk.ACTIVE))

    #def get_clicked_value(self, event=None):
     #   self.currentlySelected = self.myList.get(tk.ACTIVE)
     #   print("yupyup")

    ###THIS NEEDS TO GETS FIXED, SO THAT IT WILL ALWAYS FIND THE RIGHT LOCATION FOR THE INGREDIENT FILE
    def getlist(self):
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "r")
        for line in f:
            self.myList.insert(tk.END, line)

