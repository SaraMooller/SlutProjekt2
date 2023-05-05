import numpy as numpy
import random
import os
import tkinter.font as font
from tkinter import *
from tkinter import messagebox
import threading

class Spelklass():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.config(bg="white")
        self.font = font.Font(size=30)
        self.symbols = ["!","$","?"]
        for column in range(2):
            for row in range(3):
                index = random.randint(0,len(self.symbols)-1)
                symbol = self.symbols[index]
                button1 = Button(self.root, text=symbol, width=8, height=3, font=self.font)
                button1.grid(column=column, row=row)

if __name__ =="__main__":
    root = Tk()
    Spel=Spelklass(root)
    # Spel.Label()
    root.mainloop()