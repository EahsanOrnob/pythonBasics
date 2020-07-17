# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:00:17 2020

@author: User
"""

class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop:
            
        def __init__(self):
            self.size=15.6
            self.ram='8gb'
            self.rom='1tb'
            self.pro='i5'
                
        def show(self):
            print(self.size,self.ram,self.rom,self.pro)
        
s1=Student('ornob',56)

s1.show()
