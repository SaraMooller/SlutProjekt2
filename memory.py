import numpy as np
import tkinter.font as font
from tkinter import *
import time
import threading

class Spelklass():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500") # Storleken på boxen
        self.root.config(bg="black") # Bakgrundsfärg 
        self.font = font.Font(size=30) # Textstorlek
        self.symbols = self.lipsum(["!","$","?"]) # De olika tecknena som ska matchas 
        self.clicked = None 

        for column in range(len(self.symbols[0])):
            for row in range(len(self.symbols)):  
                button1 = Button(self.root, text="", width=8, height=3, font=self.font, bg = "pink") # Bestämmer utseende på knapparna
                button1["command"] = lambda r=row, c=column, b=button1: self.click(r, c, b) # Berättar vad knappen ska göra 
                button1.grid(column=column, row=row) # Placerar knappen i rutnät
            
    def lipsum(self, symboler: list):
        symbols = []
        symboler = symboler * 2 # Duplicerar symbolerna så att det ska kunna matchas senare
        length = len(symboler)
        for i in range(length):
            j = np.random.randint(0, len(symboler)) # Slumpar fram en symbol
            symbols.append(symboler[j]) # Lägger till symbolEN till symbols  
            del symboler[j] # Tar bort symbolEN från symbolER 
        # Ändrar formen av symbols
        return np.array(symbols).reshape(3,2) 
    
    # När en knapp klickas 
    def click(self, row, column, button):
        symbol = self.symbols[row, column]
        button["text"] = symbol
        button["state"] ="disabled" # Gör att man inte kan klicka på knapp
        if (self.clicked != None): # Kollar ifall en annan knapp är tryckt på
            if (self.symbols[row, column] == self.symbols[self.clicked[0], self.clicked[1]]): # Kollar ifall symbolerna är lika 
                # Byter färgen på bagrunden av kanppen när symbol matchar
                button["bg"] = "#9dd6e3" 
                self.clicked[2]["bg"] = "#9dd6e3"
            else:
                # Gör att den kan köra samtidigt
                thread = threading.Thread(target=clear, args=[button, self.clicked[2]])
                thread.start()
            self.clicked = None 

        else:
            # Sparar knappen till nästa knapp tryck
            self.clicked = row, column, button


def clear(button1, button2):
    time.sleep(1.5) # Tiden som den visar symbolerna 
    button1["text"] = ""  
    button2["text"] = ""  
    # Gör att man kan klicka på knapp
    button1["state"] ="normal"
    button2["state"] ="normal"
    

if __name__ =="__main__":
    root = Tk()
    Spel=Spelklass(root)
    root.mainloop() 