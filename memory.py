import numpy as np
import random
import os
import tkinter.font as font
from tkinter import *
from tkinter import messagebox
import threading

class Spelklass():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.root.config(bg="black")
        self.font = font.Font(size=30)
        self.symbols = self.lipsum(["!","$","?"])

        for column in range(len(self.symbols)):
            for row in range(len(self.symbols[0])):  
                symbol = self.symbols[column, row]
                button1 = Button(self.root, text=symbol, width=8, height=3, font=self.font, bg = "pink")
                button1.grid(column=row, row=column)
            
    def lipsum(self, symboler: list):
        symbols = []
        symboler = symboler * 2
        length = len(symboler)
        for i in range(length):
            j = np.random.randint(0, len(symboler))
            symbols.append(symboler[j])
            del symboler[j]
        # print(np.array(symbols).reshape(2,3))
        return np.array(symbols).reshape(3,2)




if __name__ =="__main__":
    root = Tk()
    Spel=Spelklass(root)
    # Spel.Label()
    root.mainloop() 