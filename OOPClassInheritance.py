#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:04:04 2020

@author: Alaisha Naidu
Name: OOP Class Inheritance
"""

class WebsiteEmailUpdate:
    
    def __init__(self, email):
        self.email = email
    
    def client_username(self, new_email):
        self.email = new_email
        
class DatabaseEmailUpdate(WebsiteEmailUpdate): #"Copy and paste code above into new class"
    pass #both classes do the same thing