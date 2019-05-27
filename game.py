
"""
Created on Sat Apr 20 01:02:59 2019

@author: Taha
"""

from minmaxAlgo import gameMinimax
from gameUtility import gameUtility
from functools import partial
from BrickBreakerSuccessorState import BrickBreakerSuccessorState 
from tkinter import *
from ManageUI import ManageUI


import copy

class BrickBreaker():
    def __init__(self,PlayerName):
        self.PlayerName=PlayerName
    
    def generateBoard(self,Width,Height):
        Width*=2
        Width-=1
        Height*=2
        Height-=1
        list = [[' ' for i in range(Width+2)] for j in range(Height+2)]
        for i in range(Height):
            for j in range(Width):
                list[i][j]='.'
                if( j%2==0 and not i%2==0):
                    list[i][j]='V'
                if( not j%2==0 and  not i%2==0):
                    list[i][j]='X'
                
                if(not j%2==0 and i%2==0):
                    list[i][j]='H'
        return list


    
    def getScore(self,arr):
        score=[]
        scoreAI=0
        scorePlayer=0
        
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if(arr[x][y]==self.PlayerName):
                    
                    scorePlayer+=10
                elif(arr[x][y]=="AI"):
                    scoreAI+=10
                    
        score.append(scorePlayer)
        score.append(scoreAI)
        
        return score

    def changeArray(self,arr,i,j):
        if(arr[int(i)][int(j)]=='V'):
            arr[int(i)][int(j)]='|'
        else:
            arr[int(i)][int(j)]='_'
        return arr
    

    def addAlphabet(self,arr,i,j,isHorizontal,letter):
        i=int(i)
        j=int(j)
        if(isHorizontal and arr[i+2][j]=='_'and arr[i+1][j+1] =='|' and arr[i+1][j-1]=='|'):
            arr[i+1][j]=letter
        if(isHorizontal and arr[i-2][j] =='_' and arr[i-1][j+1] =='|' and arr[i-1][j-1]=='|' ):
            arr[i-1][j]=letter
        if((not isHorizontal and arr[i-1][j-1]=='_'and arr[i][j-2] =='|' and arr[i+1][j-1]=='_')):
            arr[i][j-1]=letter
        if(not  isHorizontal and arr[i][j+2] =='|' and arr[i+1][j+1] =='_' and arr[i-1][j+1]=='_'  ):
            arr[i][j+1]=letter
        return arr



    

   
    



        
    