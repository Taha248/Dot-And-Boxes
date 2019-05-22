# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:57:19 2019

@author: Taha
"""

class gameUtility():
    def __init__(self):
        pass
    
    def calculateUtility(self,state,i,j,isHorizontal,isMax):
        try:
            #UTILITY ON PLACING BAR ON 3 BAR BOX
            if((isHorizontal and state[i+2][j]=='_'and state[i+1][j+1] =='|' and state[i+1][j-1]=='|') or 
               ( isHorizontal and state[i-2][j] =='_' and state[i-1][j+1] =='|' and state[i-1][j-1]=='|' )):
                if(isMax):
                    return 1000
                else:
                    return -1000                    
        
            if((not isHorizontal and state[i-1][j-1]=='_'and state[i][j-2] =='|' and state[i+1][j-1]=='_') or 
               (not  isHorizontal and state[i][j+2] =='|' and state[i+1][j+1] =='_' and state[i-1][j+1]=='_'  )):
                if(isMax):
                    return 1000
                else:
                    return -1000  
              
            #UTILITY ON PLACING BAR ON 2 BAR BOX
            if((isHorizontal and state[i+2][j]=='_' and state[i+1][j-1]=='|') or
                (isHorizontal and state[i+1][j+1]=='|' and state[i+1][j-1]=='|') or
                (isHorizontal and state[i+1][j+1]=='|' and state[i+2][j]=='_' ) or
                (isHorizontal and state[i-2][j]=='_' and state[i-1][j+1]=='|' ) or
                (isHorizontal and state[i-2][j]=='_' and state[i-1][j-1]=='|' ) or
                (isHorizontal and state[i-1][j-1]=='|' and state[i-1][j+1]=='|')):
                return -10
            
            if((not isHorizontal and state[i-1][j-1]=='_' and state[i][j-2]=='|') or
                (not isHorizontal and state[i-1][j-1]=='_' and state[i+1][j-1]=='_') or
                (not isHorizontal and state[i][j-2]=='|' and state[i+1][j-1]=='_' ) or
                (not isHorizontal and state[i-1][j+1]=='_' and state[i][j+2]=='|' ) or
                (not isHorizontal and state[i-1][j+1]=='_' and state[i+1][j+1]=='_' ) or
                (not isHorizontal and state[i][j+2]=='|' and state[i+1][j+1]=='_')):
                 return -10
             
            #UTILITY ON PLACING BAR ON 1 BAR BOX
            if((   isHorizontal and state[i+1][j-1]=='|'
                or isHorizontal and state[i+2][j]=='_' 
                or isHorizontal and state[i+1][j+1]=='_' 
                or isHorizontal and state[i-1][j-1]=='_' 
                or isHorizontal and state[i-1][j+1]=='_' 
                or isHorizontal and state[i-2][j]=='|')): 
                return 10
    
            if((    not isHorizontal and state[i][j-2]=='|' 
                or  not isHorizontal and state[i-2][j-1]=='_' 
                or  not isHorizontal and  state[i+1][j-1]=='_' 
                or  not isHorizontal and state[i-1][j+1]=='_' 
                or  not isHorizontal and  state[i+1][j+1]=='_' 
                or  not isHorizontal and  state[i][j+2]=='|')): 
                return 10        
                 
            
        except IndexError:
            print(state)
            print('ERROR' )
            print(i,j)
        
        return 100
    
    