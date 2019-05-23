# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:44:32 2019

@author: Taha
"""
from BrickBreakerSuccessorState import BrickBreakerSuccessorState 

class gameMinimax():
    def __init__(self,game,utility,successorState):
        self.game=game
        self.utility=utility
        self.successorState =successorState
        self.score=0
        self.win=False
        self.playerWin=False
        self.AIPlayerName="AI"
        self.playerWinningState=[]
        self.k=0
    def minimaxAlgo(self,state,isMax):
        self.k+=1
        self.win=False
        self.playerWin=False
        AIMoves,m,secondBestMove=[],[],[]
        AIMoves=self.successorState.successorState(state)
        badMove=False
        for move in AIMoves:
            badMove=False
            change= self.successorState.getStateChange(state,move)
           # print(change)
            if self.utility.calculateUtility(move,change[0],change[1],change[2],isMax)==1000:
                self.score+=10
                #print(self.k)
                #print(self.score)
                self.win=True
                #print("PC Score="+str(self.score))
                array=self.game.addAlphabet(move,change[0],change[1],change[2],self.AIPlayerName)
                return array
            
            PlayerMoves=self.successorState.successorState(move)
            for PlayerMove in PlayerMoves:                                              
                change=self.successorState.getStateChange(move,PlayerMove)
                if self.utility.calculateUtility(PlayerMove,change[0],change[1],change[2],not isMax)== -1000:
                    self.playerWinningState=PlayerMove
                    badMove=True
                    
                    break
            if badMove:
                secondBestMove=move
                continue
            else:
                m=move
        if not m:
            self.playerWin=True
            return secondBestMove        
        
                
        return m
    
    def isWinningState(self,oldState,newState):
        change= self.successorState.getStateChange(oldState,newState)
        i,j,isHorizontal,state=change[0],change[1],change[2],newState
    
        if((isHorizontal and state[i+2][j]=='_'and state[i+1][j+1] =='|' and state[i+1][j-1]=='|') or 
          ( isHorizontal and state[i-2][j] =='_' and state[i-1][j+1] =='|' and state[i-1][j-1]=='|' )):
            return True
                   
        
        if((not isHorizontal and state[i-1][j-1]=='_'and state[i][j-2] =='|' and state[i+1][j-1]=='_') or 
           (not  isHorizontal and state[i][j+2] =='|' and state[i+1][j+1] =='_' and state[i-1][j+1]=='_'  )):
            return True
        
        return False