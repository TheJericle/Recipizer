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

class quantityScroll(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # type: (object, object, object) -> object
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(parent)
        self.hscale   = tk.Scale(self.frame, from_=0, to= 1000)
        self.hscale.config(orient="horizontal")

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
        self.hscale.pack()

