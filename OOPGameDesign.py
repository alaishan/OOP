#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:52:09 2020

@author: Alaisha Naidu 
Name: OOP Game Design 
Creds: DataCamp 
"""

class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    def move(self, steps): #Mathod with step attribute to determine where each player is in the game
        if self.position + steps <=Player.MAX_POSITION:
            self.steps = steps
            self.position = self.position + steps
        else:
            self.position = Player.MAX_POSITION
        return self.position
              
    def draw(self): #Method to draw game in conole 
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()