# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:25:40 2019

@author: Taha
"""

class Node:
    def __init__(self,state,isMax,parent):
        self.state=state
        self.isMax=isMax
        self.parent=parent
        
    def isMax(self):
        return self.isMax