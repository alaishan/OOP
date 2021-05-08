#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:44:52 2021

@author: Alaisha Naidu
Name: OOP Class Design
Creds: DataCamp

"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        self.balance -=amount 
    
   #Makes withdrawing from each account much easier, better user interface
    def batch_withdraw(list_of_accounts, amount): #withdraws an amount from each of the accounts
        for acct in list_of_accounts:
            acct.withdraw(amount)
    
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

b, c, s = BankAccount(1000), CheckingAccount(2000, 200), SavingsAccount(3000, 0.05)
BankAccount.batch_withdraw([b,c,s], 100)
print(c.balance) #returns 1900 ##YAAAAAAAAYYYYY