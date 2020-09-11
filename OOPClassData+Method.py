#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:45:47 2020

@author: Alaisha Naidu
Name: OOP - Class Level Data and Class Methods
"""

class LocalBusinesses: 
    MIN_EMPLOYEES = 1 #Nin number of employees 
    def __init__(self, business_name, employees):
        self.business_name = business_name 
        if employees >= LocalBusinesses.MIN_EMPLOYEES:
            self.employees = employees
        else: 
            self.employees = LocalBusinesses.MIN_EMPLOYEES
            
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f: 
            name = f.readline()
            return cls(name)