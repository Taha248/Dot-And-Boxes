# -*- coding: utf-8 -*-
"""
Created on Mon May 27 06:37:48 2019

@author: Taha
"""
import copy
from tkinter import *
from BrickBreakerSuccessorState import BrickBreakerSuccessorState 

class ManageUI():
    def __init__(self,board,master,canvas,minmax,game,arr):
        self.board = board
        self.master = master
        self.canvas = canvas
        self.minmax= minmax
        self.game= game
        self.arr=arr
    
# =============================================================================
#     Below Function changes canvas through following procedure:
#         1)First Gets Changed 2d Array on the Line Clicked
#         2)if the Change Makes the player win a block then its Player turn again
#         3)if it does not make the Player win a block then 
#         4)Execute minmax Algorithm to get next AI Best Move and Build that Board 
#         5)if the AI Player wins a block then calculate AI Best Move and Repeat (Loop)
#         6)Represent 2d on the board
# =============================================================================
    
    def changeCanvas(self,X,Y):
        newArr=copy.deepcopy(self.arr)
        changedArray=self.game.changeArray(self.arr,X,Y)
        
        if(self.minmax.isWinningState(newArr,changedArray)):
            change=BrickBreakerSuccessorState().getStateChange(newArr,changedArray)
            changedArray=self.game.addAlphabet(changedArray,change[0],change[1],change[2],self.game.PlayerName)
            self.board.buildBoardUI(changedArray,self.canvas,True)
            self.board.lbl_ScoreP['text']=str(self.game.PlayerName)+" Score= "+str(self.game.getScore(self.arr)[0])
        else:
            newArray=self.minmax.minimaxAlgo(changedArray,True)
            self.board.buildBoardUI(newArray,self.canvas,False)
            self.arr=newArray
            
        while(True):
            if(not self.minmax.win):
                break
            newArray=self.minmax.minimaxAlgo(newArray,True)
            if newArray:
                self.board.buildBoardUI(newArray,self.canvas,False)
            self.arr=newArray
    
    
    def createLine(self,x,y):
        self.changeCanvas(x,y)