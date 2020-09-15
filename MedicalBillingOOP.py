#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:59:32 2020

@author: Alaisha Naidu
Name: Medical Billing OOP
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
            print("Remaining Medical Aid balance is:")
        else:
            self.medical_aid_balance = self.medical_aid_balance
            print("Not enough Medical Aid Funds, current balance is:")

class Cardiologist(Specialist):
    pass

class Dentist(Specialist):
    pass