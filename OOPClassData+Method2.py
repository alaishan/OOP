#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:45:47 2020

@author: Alaisha Naidu
Name: OOP - Class Level Data and Class Methods
"""
import pandas as pd

class LocalBusinesses: 
    MIN_EMPLOYEES = 1 #Min number of employees 
    def __init__(self, business_name, employees):
        self.business_name = business_name 
        if employees >= LocalBusinesses.MIN_EMPLOYEES:
            self.employees = employees
        else: 
            self.employees = LocalBusinesses.MIN_EMPLOYEES
            
    @classmethod
    def extract_tables_to_df(cls, pathname1):
        emails_df = pd.read_csv(pathname1, sep = ";", usecols=["Email"])
        return emails_df
        
client = LocalBusinesses.extract_tables_to_df('/Users/user/Desktop/SampleData.csv')
type(client)