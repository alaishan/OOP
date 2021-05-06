#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:32:00 2021

@author: Alaisha Naidu
Name: Exceptions
Creds: DataCamp

"""

class BalanceError(Exception): pass #create an empty class

class Customer:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError("Balance has to be non-negative.") #raise an error if a condition is not being met
        else: 
            self.name, self.balance = name, balance

customer = Customer("Lucy", -5)

#Retruns customized error: 
#BalanceError: Balance has to be non-negative.