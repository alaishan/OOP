#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:56:13 2021

@author: Alaisha Naidu
Name: Customizing Functionality
Credits: DataCamp
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        self.balance -=amount 
    
class SavingsAccount(BankAccount):
    #Constructor for Savings Account 
    def __init__(self, balance, interest_rate):
        #First run code for creating a Bank Account - call constructor from Parent class
        BankAccount.__init__(self, balance) #self in this case is a Savings Account but also a Bank Account
        #Add more functionality
        self.interest_rate = interest_rate
    
    #New functionality
    def compute_interest(self, n_periods = 1):
        return self.balance*((1+self.interest_rate)**n_periods-1)

class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount, fee=0):
        if fee <= self.limit:
            BankAccount.withdraw(self, amount + fee)
        else:
            BankAccount.withdraw(self, amount + self.limit)
            

acct = SavingsAccount(1000, 0.03)
print(acct.interest_rate)

check_acct = CheckingAccount(1000, 25)
check_acct.withdraw(200, fee = 15)
print(check_acct.balance)