  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:31:04 2020
@author: Alaisha Naidu
Name: Class inheritance, Method Inheritance
Creds: DataCamp
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance - amount
        
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        BankAccount.__init__(self, balance)
        
    def withdraw(self, amount, fee, limit):
        if limit > fee: #set a condition fro code to execute
            new_balance = BankAccount.withdraw(self, amount - fee)
        return new_balance
    
transact1 = SavingsAccount(1000)
transact1.withdraw(400, 5, 6)

#transact2 = BankAccount(1000)
#transact2.withdraw(400,5)   #Produces error here because no fee applicable in BankAccount class