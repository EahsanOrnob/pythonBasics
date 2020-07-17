# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:37:33 2020

@author: User
"""


class Student:
    
    school='SKG' #class variable
    
    def __init__(self,m1,m2,m3):
        
        self.m1=m1 #instance Variable
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    #excesor / #instance Method
    def get_m1(self):
        return self.m1
    #mutator / #instance Method
    def set_m1(self,value):
        self.m1= value
        
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("Info has nothing to do")



s1=Student(13,14,15)

print(s1.get_m1())

s1.set_m1(70)


print(s1.get_m1())

print(s1.avg())

print(Student.getSchool())
Student.info()