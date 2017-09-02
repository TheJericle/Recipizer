#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from _future_ import absolute_import, division, print_function

# Import Recipizer modules
from .core.Recipe_Book_Class import RecipeBook

# -----------------------------------------------------------------

filename = "Recipe_Book.txt"

New_Recipe_Book = RecipeBook()

New_Recipe_Book.parser(filename)

print len(New_Recipe_Book._Recipe_List)

# -----------------------------------------------------------------
