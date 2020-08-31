#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:02:18 2020

@author: Alaisha Naidu
Name: Object Oriented Programming
"""

class client:
    #Set name attribute of a client object to new name
    def set_name(self, new_name): #self is a stand-in for an object that does not yet exist
        self.name = new_name 
    #Using .name from the object it*self*
    def identify(self):
        print("This is " + self.name)

client1 = client()
client1.set_name('Tukiyas Closet')
client1.identify()