#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from _future_ import absolute_import, division, print_function

# Import external modules
from Tkinter import *

# -----------------------------------------------------------------

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill =Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()

# -----------------------------------------------------------------
