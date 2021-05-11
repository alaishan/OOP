#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:09:42 2021

@author: Alaisha Naidu
Name: OOP Properties
Creds: DataCamp

"""

class Employee:
    def __init__(self, name, new_salary):
        self._salary = new_salary  #protected atritube salary with leading _ to store data
    
    @property #decorator returns the data
    def salary(self): #method name is the exact of the restricted attribute
        return self._salary 

    @salary.setter # decorator implements validation and sets the attribute
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid Salary") #salary cannot be negative or 0
        self.salary = new_salary
        
emp = Employee("Shreya K", 3500)
print(emp.salary) #access the property
#emp.salary = 6000 # assigns a value to the salary using the @salary.setter property
emp.salary = -300 # raises exception

# without @attr.setter property, creates read only data
# @attr.getter used when property value is being retrieved
# @attr.deleter used when property is being deleted using del