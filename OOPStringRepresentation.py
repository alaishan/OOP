#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:51:00 2021

@author: Alaisha Naidu
Name: Operator Overloading: String Representation
Creds: DataCamp

"""

#printing the object dislays the address in memory by default
#printing an array shows more meaningful information - the content of the array/data contained in the object

#the methods __str__() and __repr__() returns a printable representation of an object

class Customer:
    def __init__(self, name, balance):
        self.name, self.balance = name, balance
    
    def __str__(self): #str is more informal and used for end user 
        cust_str="""
        Customer:       
            name: {name}
            balance: {balance}
        """.format(name = self.name, balance = self.balance)
        return cust_str

class Customers:
    def __init__(self, name, balance):
        self.name, self.balance = name, balance
        
    def __repr__(self): #the point of repr is to give the exact call needed to reproduce the object ie '' around name
        return "Customers('{name}', {balance})".format(name = self.name, balance = self.balance)

cust = Customer("Maryam Azar", 3000)
print(cust)
            
#Retruns the following:
#        Customer:       
#            name: Maryam Azar
#            balance: 3000     

custs = Customers("Maryam Azar", 3000)
print(custs) #implicitly calls repr      

#Retruns the folowing:
# Customers('Maryam Azar', 3000)