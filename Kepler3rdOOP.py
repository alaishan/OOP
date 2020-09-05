#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:59:50 2020

@author: Alaisha Naidu
Name: Kepler's Third Law - Satellite orbits 
Creds: University of Cape Town
"""
import math
from math import pi, sqrt


class KeplerThird: 
    
    def __init__(self, T=43080, a=26571000, G=5.972E24, M=6.674E-11):
        self.T = T 
        self.a = a
        self.G = G
        self.M = M
    
    def radius(self):
        T2 = self.T*self.T
        denom = 4*pi*pi
        g = self.G
        m = self.M
        r1 = (T2*g*m)/denom
        radius = r1**(1/3)
        return radius 
    
a1 = KeplerThird(T=43200)   
print("a1 = ", a1.radius(), "meters") 
a2 = KeplerThird(T=42960)
print("a2 = ", a2.radius(), "meters") 
change = a1.radius() - a2.radius()      
print("Change in orbital radius in meters is", change)