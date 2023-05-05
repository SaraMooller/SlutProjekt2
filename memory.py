import numpy as numpy
import random
import os
from tkinter import *
from tkinter import messagebox
import threading

class Spelklass(Tk):
    def __init__(self):
    self.geometry("600x600")
    self.config(bg="white")

if __name__=="__main__":
    Spel=Spelklass()
    Spel.Label()
    Spel.mainloop