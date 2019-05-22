# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:34:31 2019

@author: Taha
"""
"""
Created on Sat Apr 20 01:02:59 2019

@author: Taha
"""

from minmaxAlgo import gameMinimax
from gameUtility import gameUtility
from functools import partial
from BrickBreakerSuccessorState import BrickBreakerSuccessorState 
from tkinter import *
import copy

class BrickBreaker():
    def __init__(self,PlayerName):
        self.PlayerName=PlayerName
        self.PlayerScore=0
        
        
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
    
arr=[]
colors=[]

def changeArray(arr,i,j):
    if(arr[int(i)][int(j)]=='V'):
        arr[int(i)][int(j)]='|'
    else:
        arr[int(i)][int(j)]='_'
    return arr


        
    
def changeCanvas(X,Y):
    global arr,w,x,game,lbl_ScoreP
   # val = mystring.get()
    #index=val.split(",")
    newArr=copy.deepcopy(arr)
    changedArray=changeArray(arr,X,Y)
    if(x.isWinningState(newArr,changedArray)):
        change=successorState.getStateChange(newArr,changedArray)
        changedArray=game.addAlphabet(changedArray,change[0],change[1],change[2],"P")
        
        buildBoardUI(changedArray,w,True)
        game.PlayerScore+=10
        lbl_ScoreP['text']=str(game.PlayerName)+" Score= "+str(game.PlayerScore)
    else:
        newArray=x.minimaxAlgo(changedArray,True)
        buildBoardUI(newArray,w,False)
        arr=newArray
        
        
    while(True):
        if(not x.win):
            break
        newArray=x.minimaxAlgo(newArray,True)
        buildBoardUI(newArray,w,False)
        arr=newArray

btnDict={}

def createLine(x,y):
    global btnDict
    changeCanvas(x,y)
    
    
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

    
    
newBoard=True
def buildBoardUI(arr,w,isPlayer): 
    global newBoard       
    global lbl_ScoreAI,miniMax,master,btnDict
    lbl_ScoreAI['text']="AI Score= "+str(miniMax.score)
    
 #   RowX1 = 40
    RowY1 = 60
  #  RowX2 = 35
    RowY2 = 55
    
    
    for x in range(len(arr)-2):
        RowX1 = 60
        RowX2 = 55        
        for y in range(len(arr[x])-2):
            if(arr[x][y]=='H'):
                i=(y*40)+26
                j=(x*40)+42
                if(newBoard):
                    btn = Button ( master ,bg="gainsboro" ,borderwidth=0,width=8, height=1)                                
                    btn.place(x=i,y=j)
                    btn.config(command=partial(createLine,x,y))
                    btnDict[x,y]= btn

            if(arr[x][y]=='V'):
                i=(y*40)+50+1
                j=(x*41)+21
                if(newBoard):
                    btn = Button( master ,bg="gainsboro" ,borderwidth=0,width=1, height=3)
                    btn.place(x=i,y=j)
                    btn.config(command=partial(createLine,x,y))
                    btnDict[x,y]= btn
                
                
            if(arr[x][y]=='_'):
                btnDict[x,y].place(x=999,y=999)
                w.create_line(RowX1-40,RowY1-3 , RowX2+46, RowY1-3, width=5,fill="blue")
                
            if(arr[x][y]=='|'):
                btnDict[x,y].place(x=999,y=999)
                w.create_line(RowX1-2,RowY1-41 , RowX1-2, RowY2+41, width=5,fill="blue")
            if(arr[x][y]!='X' and arr[x][y]!='H' and  arr[x][y]!='V' and  arr[x][y]!='.'and  arr[x][y]!='_'and  arr[x][y]!='|'):
                w.create_text(RowX1,RowY1, text=arr[x][y], fill="red", font="Arial 20")
            if x%2==0 and y%2==0:
                w.create_oval(RowX1,RowY1, RowX2, RowY2, fill="red")
            
            
            RowX1+=40
            RowX2+=40
        RowY1+=40
        RowY2+=40
    newBoard=False
    
game = BrickBreaker("P1")

Width =  5
Height = 5
arr=game.generateBoard(Width,Height)


utility=gameUtility()
successorState=BrickBreakerSuccessorState()
x=gameMinimax(game,utility,successorState)
miniMax=x

master = Tk()
master.title("Dot & Boxes")
master.resizable(0, 0)

master.geometry(str(Width*90)+"x"+str((Height*100)+40)+"+300+20")
w = Canvas(master, width=Width*100, height=(Height*100)-60 , bg="gainsboro")

w.pack()


lbl_ScoreP=Label(master, text="P1 Score= 0 ",font=('Arial', 13), foreground="green")
lbl_ScoreAI=Label(master, text="AI Score= 0 ",font=('Arial', 13), foreground="blue")
#l2=Label(master, text="Enter X and Y Axis (eg. 1,2 )").pack()
lbl_ScoreP.place(x = (Width*90)/2, y = (Height*100)-30 , width=120, height=25,anchor="center")
lbl_ScoreAI.place(x = (Width*90)/2, y = (Height*100)-5 , width=120, height=25,anchor="center")



    
#btn = Button ( master ,text="Enter",command=changeCanvas).pack()
buildBoardUI(arr,w,False)
#btn = Button ( master ,text="Enter1",command=changeCanvas).place(x=0,y=10)
#btn = Button ( master ,text="Enter1",command=changeCanvas).place(x=50,y=10)
#btn = Button ( master ,text="Enter1",command=changeCanvas).place(x=100,y=10)
#btn = Button ( master ,text="Enter1",command=changeCanvas).place(x=150,y=10)
mainloop()


    




        
    