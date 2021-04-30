#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:33:52 2021

@author: Alaisha Naidu
Name: Operator Overloading: Comparison
Creds: DataCamp

"""

class Customer: 
    def __init__(self, name, balance, id):
        self.name, self.balance = name, balance
        self.id = id

customer1 = Customer("Maryam Azar", 300, 123)
customer2 = Customer("Maryam Azar", 300, 123)

print(customer1 == customer2) #comparing references, not the data 
# returns false becasue customer data is stored at different places in memory even though the data is the same

print(customer1)
# returns <__main__.Customer object at 0x7fd0deac52e0> which is a hexadecimal number for the address of where the data is stored
print(customer2)
# returns <__main__.Customer object at 0x7fd0deac5fa0> which is not the same as above

import numpy as np 
array1 = np.array([1,2,3])
array2 = np.array([1,2,3])

array1 == array2
#returns true, because the data is being compared. Same with Pandas DF and other objects

# Define a special method to compare custom classes
class Customers:
    def __init__(self, id, name):
        self.id, self.name = id, name
    def __eq__(self, other): #called whenever 2 objects of a class are being compared to each other
        print("__eq__ is called")
        #Returns Boolean (True/False)
        return print((self.id == other.id) and (self.name == other.name))

customer1 = Customers(123, "Maryam Azar")
customer2 = Customers(123, "Maryam Azar")

customer1 == customer2 #returns true