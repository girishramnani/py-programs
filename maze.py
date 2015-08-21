# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:51:03 2015

@author: Girish
"""


import random 
import numpy
import tkinter
import sys


White = 0
Gray = 1
Black =2

class Maze(object):
    
    def __init__(self,height,width,size):
        
        self.height = height
        self.width = width
        self.size = size
        self.num_rows = height//size
        self.num_cols = width//size
    

    def view(self):
        master = tkinter.Tk()
        w = tkinter.Canvas(master,width=self.width+10,height=self.height+10)
        
    
    def dfs(self,point):
        path = [point]
        
        while path:
            cell = path[0]
            if  self.color[cell]==White:
                
                neighbours = self.neighbour(cell)
                if len(neighbours) > 0:
                    
                
                
                
            
            
    def construct(self):
        
        for r in self.num_rows:
            for c in self.num_cols:
        self.color={()}
        
        