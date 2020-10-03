#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:59:32 2020

@authors: Alaisha Naidu and Tony Naidu
Name: Medical Billing OOP - Class Inheritance Class Customization
"""
         
class Specialist:
    def __init__(self, medical_aid_balance):
        self.medical_aid_balance = medical_aid_balance
        
    def medical_aid_claim(self, consultation, prescription, medical_tests, radiology_referral, blood_tests):
        self.consultation = consultation
        self.prescription = prescription
        self.medical_tests = medical_tests
        self.radiology_referral = radiology_referral
        self.blood_tests = blood_tests
        if self.consultation + self.prescription + self.medical_tests + self.radiology_referral + self.blood_tests <= self.medical_aid_balance:
            self.medical_aid_balance = self.medical_aid_balance - (self.consultation + self.prescription + self.medical_tests + self.radiology_referral + self.blood_tests)
            print("Payment Successful. Remaining Medical Aid balance is:\n", self.medical_aid_balance)
        else:
            self.medical_aid_balance = self.medical_aid_balance
            print("Payment unsuccessful. Not enough Medical Aid Funds, current balance is:\n", self.medical_aid_balance)
        return self.medical_aid_balance
    
    def in_hospital_benefit(self, hospital_cover_balance, ward_fees, theatre_fees, drugs, radiolology_fee):
        self.hospital_cover_balance = hospital_cover_balance
        self.ward_fees = ward_fees
        self.theatre_fees = theatre_fees
        self.drugs = drugs
        self.radiolology_fee = radiolology_fee
        if self.hospital_cover_balance >= self.ward_fees + self.ward_fees + self.theatre_fees + self.drugs + self.radiolology_fee:
            self.hospital_cover_balance = self.hospital_cover_balance - (self.ward_fees + self.ward_fees + self.theatre_fees + self.drugs + self.radiolology_fee)
            print("Payment Successful. Remaining In-Hospital Benefit balance is:\n", self.hospital_cover_balance)
        else:
            self.hospital_cover_balance = self.hospital_cover_balance
            print("Payment unsuccessful. Not enough In-Hospital Benefit Funds, current balance is:\n", self.hospital_cover_balance)
        return self.hospital_cover_balance
        
    
class Cardiologist(Specialist):
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, pacemaker, stent):
        Specialist.__init__(self, medical_aid_balance)
        self.pacemaker = pacemaker
        self.stent = stent
    
    def operation_cost(self, pacemaker, stent):
        return self.pacemaker + self.stent
    

class Dentist(Specialist):
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, teeth_whitinging, cavity_refill):
        Specialist.__init__(self, medical_aid_balance)
        self.teeth_whitinging = teeth_whitinging
        self.cavity_refill = cavity_refill
        
        def proceedures(self, teeth_whitinging, cavity_refill):
            return self.teeth_whitinging + self.cavity_refill

class Neurologist(Specialist):
    pass
    
class Optometrist(Specialist):
    def __init__(self, medical_aid_balance, contact_lenses, spectacles):
        Specialist.__init__(self, medical_aid_balance)
        self.contact_lenses = contact_lenses
        self.specatcles = spectacles
        
        def eye_wear(self, constact_lenses, spectacles):
            return self.spectacles + self.contact_lenses
       
        def medical_aid_claim(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, fee):
            new_balance = Specialist.medical_aid_claim(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance - fee)
            return new_balance
        
class GeneralSurgeon(Specialist):
    pass

patient1 = Optometrist(7600, 5, 8)
patient1.medical_aid_claim(6, 7, 8, 4, 40)







