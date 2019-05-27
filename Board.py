# -*- coding: utf-8 -*-
"""
Created on Mon May 27 06:41:15 2019

@author: Taha
"""
from game import BrickBreaker
from minmaxAlgo import gameMinimax
from gameUtility import gameUtility
from functools import partial
from BrickBreakerSuccessorState import BrickBreakerSuccessorState 
from tkinter import *
from ManageUI import ManageUI

class Board():
    def __init__(self , master,width,height,PlayerName): 
        self.WIDTH=width
        self.HEIGHT=height
        self.window=master
        self.arr=[]
        self.btnDic={} #Dictionary for Clicable Lines
        self.newBoard=True
        self.PlayerName=PlayerName
        self.initializeUI()
    
    def initializeUI(self):
        
        canvas = Canvas(self.window, width=self.WIDTH*100, height=(self.HEIGHT*100)-60 , bg="gainsboro")
        
        self.game = BrickBreaker(self.PlayerName)
        self.arr=self.game.generateBoard(self.WIDTH,self.HEIGHT)
        
        utility=gameUtility()
        successorState=BrickBreakerSuccessorState()
        
        self.x=gameMinimax(self.game,utility,successorState)
        self.ManageUI = ManageUI(self,self.window,canvas,self.x,self.game,self.arr)
        
        self.window.title("Dot & Boxes")
        self.window.resizable(0, 0)
        
        self.window.geometry(str(self.WIDTH*90)+"x"+str((self.HEIGHT*100)+40)+"+300+20")
        canvas.pack()
        
        self.lbl_ScoreP=Label(self.window, text="P1 Score= 0 ",font=('Arial', 13), foreground="green")
        self.lbl_ScoreAI=Label(self.window, text="AI Score= 0 ",font=('Arial', 13), foreground="blue")
        self.lbl_ScoreP.place(x = (self.WIDTH*90)/2, y = (self.HEIGHT*100)-30 , width=120, height=25,anchor="center")
        self.lbl_ScoreAI.place(x = (self.WIDTH*90)/2, y = (self.HEIGHT*100)-5 , width=120, height=25,anchor="center")
        self.buildBoardUI(self.arr,canvas,False)
        
        
    
    def buildBoardUI(self,arr,canvas,isPlayer): 
        global btnDict
        
        self.lbl_ScoreAI['text']="AI Score= "+str(self.game.getScore(arr)[1])
        RowY1 = 60
        RowY2 = 55
        for x in range(len(arr)-2):
            RowX1 = 60
            RowX2 = 55        
            for y in range(len(arr[x])-2):
                if(arr[x][y]=='H'):
                    i=(y*40)+26
                    j=(x*40)+42
                    if(self.newBoard):
                        btn = Button ( self.window ,bg="gainsboro" ,borderwidth=0,width=8, height=1)                                
                        btn.place(x=i,y=j)
                        btn.config(command=partial(self.ManageUI.createLine,x,y))
                        self.btnDic[x,y]= btn
    
                if(arr[x][y]=='V'):
                    i=(y*40)+50+1
                    j=(x*41)+21
                    if(self.newBoard):
                        btn = Button( self.window ,bg="gainsboro" ,borderwidth=0,width=1, height=3)
                        btn.place(x=i,y=j)
                        btn.config(command=partial(self.ManageUI.createLine,x,y))
                        self.btnDic[x,y]= btn
                    
                    
                if(arr[x][y]=='_'):
                    self.btnDic[x,y].place(x=999,y=999)
                    canvas.create_line(RowX1-40,RowY1-3 , RowX2+46, RowY1-3, width=5,fill="blue")
                    
                if(arr[x][y]=='|'):
                    self.btnDic[x,y].place(x=999,y=999)
                    canvas.create_line(RowX1-2,RowY1-41 , RowX1-2, RowY2+41, width=5,fill="blue")
                if(arr[x][y]!='X' and arr[x][y]!='H' and  arr[x][y]!='V' and  arr[x][y]!='.'and  arr[x][y]!='_'and  arr[x][y]!='|'):
                    canvas.create_text(RowX1,RowY1, text=arr[x][y], fill="red", font="Arial 20")
                if x%2==0 and y%2==0:
                    canvas.create_oval(RowX1,RowY1, RowX2, RowY2, fill="red")
                
                
                RowX1+=40
                RowX2+=40
            RowY1+=40
            RowY2+=40
        self.newBoard=False
    