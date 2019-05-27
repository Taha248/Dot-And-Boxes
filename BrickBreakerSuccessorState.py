# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:09:03 2019

@author: Taha
"""
import copy

class BrickBreakerSuccessorState():
    def __init__(self):pass
    

# =============================================================================
# Below function generates Successor Nodes from each 2d state
# =============================================================================

    def successorState(self,arr):
        nextMoves=[]
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if(arr[x][y]=='H'):
                    temp=[]
                    temp=copy.deepcopy(arr)
                    temp[x][y]='_'
                    nextMoves.append(temp)
    
                if(arr[x][y]=='V'):
                    temp=[]
                    temp=copy.deepcopy(arr)
                    temp[x][y]='|'
                    nextMoves.append(temp)
    
                    
        
        return nextMoves
    
    def isTerminalState(self,state):
        
        for x in range(len(state)):
            for y in range(len(state[x])):
                if(state[x][y]=='V' or state[x][y]=='H' ):
                    return False
        
        return True
    
        
    
    def getStateChange(self,state,nextState):
        change=[]
        for x in range(len(state)):
            for y in range(len(state[x])):
                if(not state[x][y]==nextState[x][y]):
                    change.append(x)
                    change.append(y)
                    if(nextState[x][y]=='_'):
                        change.append(True)
                    else:
                        change.append(False)
        #print(change)
        return change



