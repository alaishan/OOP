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
    
    def InHospitalBenefit(self, hospital_cover_balance, ward_fees, theatre_fees, drugs, radiolology_fee):
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
        Specialist.__init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance)
        self.pacemaker = pacemaker
        self.stent = stent
    
    def OperationCost(self, pacemaker, stent):
        return self.pacemaker + self.stent
    

class Dentist(Specialist):
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, teeth_whitinging, cavity_refill):
        Specialist.__init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance)
        self.teeth_whitinging = teeth_whitinging
        self.cavity_refill = cavity_refill
        
        def Proceedures(self, teeth_whitinging, cavity_refill):
            return self.teeth_whitinging + self.cavity_refill
    pass

class Neurologist(Specialist):
    pass
    
class Optometrist(Specialist):
    def __init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance, contact_lenses, spectacles
        ):
        Specialist.__init__(self, consultation, prescription, medical_tests, radiology_referral, blood_tests, medical_aid_balance)
        self.contact_lenses = contact_lenses
        self.specatcles = spectacles
        
        def EyeWear(self, constact_lenses, spectacles):
            return self.spectacles + self.contact_lenses

class GeneralSurgeon(Specialist):
    pass

patient1 = Cardiologist(500, 126, 0, 0, 0, 7600, 0, 0)
patient1.MedicalAidClaim()







