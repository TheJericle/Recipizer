#!/usr/bin/env python
# -*- coding: utf8 -*-
# ******************************************
# **       RECIPIZER                      **
# **       © 2017                         **
# ******************************************

# Ensure Python 3 compatibility
from __future__ import absolute_import, division, print_function

# -----------------------------------------------------------------

class Ingredient(object):

    def __init__(self, name="", quantity=0, unit=""):
        self._name = name
        self._quantity = quantity
        self._unit = unit

    def __eq__(self, other):
        if self.name != other.name:
            return False
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Pretty sure the name of the ingredient should be a string...")
        else:
            self._name = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, float):
            raise TypeError("Try using a float for the quantity")
        else:
            self._quantity = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if not isinstance(value, str):
            raise TypeError("Try using a string for the unit...")
        else:
            self._unit = value

    def inverse_parser(self):

        output = self.name + "\t" + str(self.quantity) + "\t" + self.unit
        return output

    def parser(self, v_str):
        self.name = v_str[0]
        self.quantity = float(v_str[1])
        self.unit = v_str[2]

# -----------------------------------------------------------------
