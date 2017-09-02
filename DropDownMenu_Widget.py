from Tkinter import *
import os


class DropDownMenu(object):

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.scrollbar = Scrollbar(self.frame)
        self.myList = Listbox(self.frame, yscrollcommand=self.scrollbar.set)

        self.myList.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(side=LEFT, fill=Y)

        self.getlist()
        self.scrollbar.config(command=self.myList.yview)

    def getlist(self):
        cdir = os.getcwd()
        filename = "Ingredients.txt"

        fileloc = os.path.join(cdir, filename)

        f = open(fileloc, "r")
        for line in f:
            self.myList.insert(END, line)

