#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:59:32 2020

@authors: Alaisha Naidu and Tony Naidu
Name: Medical Billing OOP - Class Inheritance Class Customization
"""
         
class Specialist:
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance):
        self.consultation = consultation
        self.prescription = prescription
        self.medical_tests = medical_tests
        self.radiology_referral = radiology_referral
        self.blood_tests = blood_tests
        self.medical_aid_balance = medical_aid_balance
        
    def MedicalAidClaim(self):
        if self.consultation + self.prescription + self.medical_tests + self.radiology_referral + self.blood_tests <= self.medical_aid_balance:
            self.medical_aid_balance = self.medical_aid_balance - (self.consultation + self.prescription + self.medical_tests + self.radiology_referral + self.blood_tests)
            print("Payment Successful. Remaining Medical Aid balance is:\n", self.medical_aid_balance)
        else:
            self.medical_aid_balance = self.medical_aid_balance
            print("Payment unsuccessful. Not enough Medical Aid Funds, current balance is:\n", self.medical_aid_balance)
        return self.medical_aid_balance
    
class Cardiologist(Specialist):
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, pacemaker, stent):
        Specialist.__init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance)
        self.pacemaker = pacemaker
        self.stent = stent
    
    def OperationCost(self, pacemaker, stent):
        return self.pacemaker + self.stent
    

class Dentist(Specialist):
    pass

class Neurologist(Specialist):
    pass

class Optometrist(Specialist):
    pass

class GeneralSurgeon(Specialist):
    pass

patient1 = Cardiologist(500, 126, 0, 0, 0, 7600, 0, 0)
patient1.MedicalAidClaim()