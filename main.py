# -*- coding: utf-8 -*-
"""
Created on Mon May 27 06:47:52 2019

@author: Taha
"""
from Board import Board
from tkinter import *

if __name__=="__main__":
    master = Tk()
    
    #Initialize Board with width , height and Player Name
    board = Board(master,4,4,"P1")
    
    master.mainloop()
