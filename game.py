
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



class Board():
    def __init__(self , master): 
        global arr
        
        Width =  4
        Height = 4
        
        w = Canvas(master, width=Width*100, height=(Height*100)-60 , bg="gainsboro")
        self.test = test(self,master,w)
        self.game = BrickBreaker("P1")
        arr=game.generateBoard(Width,Height)
        
        utility=gameUtility()
        successorState=BrickBreakerSuccessorState()
        x=gameMinimax(game,utility,successorState)
        miniMax=x
        
        master.title("Dot & Boxes")
        master.resizable(0, 0)
        
        master.geometry(str(Width*90)+"x"+str((Height*100)+40)+"+300+20")
        w.pack()
        
        
        self.lbl_ScoreP=Label(master, text="P1 Score= 0 ",font=('Arial', 13), foreground="green")
        self.lbl_ScoreAI=Label(master, text="AI Score= 0 ",font=('Arial', 13), foreground="blue")
        self.lbl_ScoreP.place(x = (Width*90)/2, y = (Height*100)-30 , width=120, height=25,anchor="center")
        self.lbl_ScoreAI.place(x = (Width*90)/2, y = (Height*100)-5 , width=120, height=25,anchor="center")
        self.buildBoardUI(arr,w,False)
    
    def buildBoardUI(self,arr,w,isPlayer): 
        global lbl_ScoreAI,miniMax,master,btnDict,game,newBoard
        self.lbl_ScoreAI['text']="AI Score= "+str(game.getScore(arr)[1])
        RowY1 = 60
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
                        btn.config(command=partial(self.test.createLine,x,y))
                        btnDict[x,y]= btn
    
                if(arr[x][y]=='V'):
                    i=(y*40)+50+1
                    j=(x*41)+21
                    if(newBoard):
                        btn = Button( master ,bg="gainsboro" ,borderwidth=0,width=1, height=3)
                        btn.place(x=i,y=j)
                        btn.config(command=partial(self.test.createLine,x,y))
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
    
    

arr=[]
colors=[]
btnDict={}
newBoard=True




class test:
    def __init__(self,board,master,canvas):
        self.board = board
        self.master = master
        self.canvas = canvas
    
    def changeArray(self,arr,i,j):
        if(arr[int(i)][int(j)]=='V'):
            arr[int(i)][int(j)]='|'
        else:
            arr[int(i)][int(j)]='_'
        return arr
    
    def changeCanvas(self,X,Y):
        global arr,w,x,game,lbl_ScoreP
        newArr=copy.deepcopy(arr)
        changedArray=self.changeArray(arr,X,Y)
        
        if(x.isWinningState(newArr,changedArray)):
            change=BrickBreakerSuccessorState().getStateChange(newArr,changedArray)
            changedArray=game.addAlphabet(changedArray,change[0],change[1],change[2],game.PlayerName)
            self.board.buildBoardUI(changedArray,self.canvas,True)
            self.board.lbl_ScoreP['text']=str(game.PlayerName)+" Score= "+str(game.getScore(arr)[0])
        else:
            newArray=x.minimaxAlgo(changedArray,True)
            self.board.buildBoardUI(newArray,self.canvas,False)
            arr=newArray
            
            
        while(True):
            if(not x.win):
                break
            newArray=x.minimaxAlgo(newArray,True)
            if newArray:
                self.board.buildBoardUI(newArray,self.canvas,False)
            arr=newArray
    
    
    def createLine(self,x,y):
        global btnDict
        self.changeCanvas(x,y)
        


    
if __name__=="__main__":
    master = Tk()
    board = Board(master)
    master.mainloop()
   
    



        
    