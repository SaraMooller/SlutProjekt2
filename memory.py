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
        self.i = 0

        for column in range(len(self.symbols)):
            for row in range(len(self.symbols[0])):  
                button1 = Button(self.root, text="", width=8, height=3, font=self.font, bg = "pink")
                button1["command"]=lambda r=row, c=column, b=button1: self.click(r, c, b)
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
    
    def click(self, row, column,button):
        print(self.i % 2 == 0)
        self.i += 1
        symbol = self.symbols[column,row]
        button["text"] = symbol
    
        print(row, column)

    
    





if __name__ =="__main__":
    root = Tk()
    Spel=Spelklass(root)
    # Spel.Label()
    root.mainloop() 