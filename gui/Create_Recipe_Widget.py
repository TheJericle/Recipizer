from Tkinter import *
from Add_Ingredient_Widget import AddIngredientWidget
from DropDownMenu_Widget import DropDownMenu

class CreateRecipeWidget(object):

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.addIngredientWidget = AddIngredientWidget(self.frame)
        self.Known_Ingredients = DropDownMenu(self.frame)





root = Tk()

CreateRecipeWidget(root)

root.mainloop()
