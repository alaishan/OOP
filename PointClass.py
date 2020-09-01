#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:06:33 2020

@author: Alaisha Naidu
Name: Point Class - OOP
Creds: DataCamp
"""


from math import sqrt


class Point: #For classes use CamelCase
    
    def __init__(self, x=0, y=0): #Always use self for self
        self.x = x #initialize attrbutes in __init__ method
        self.y = y
    
    def distance_to_origin(self): #calculates the distance to the origin 
        return sqrt(((self.x)*(self.x))+((self.y)*(self.y)))
    
    def reflect(self, axis): #refelcts point about an axis
        self.axis = axis
        if self.axis == "x":
            self.y = -self.y
        elif self.axis == "y":
            self.x = -self.x
        else:
            print("Invalid entry!")

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())