# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:58:56 2020

@author: User
"""


class Car:
    
    wheels=4
    
    def __init__(self):
        self.com='BMW'
        self.mil=10
    
    def update(self):
        self.wheels=3
    
c1=Car()
c2=Car()

#c1.update()
c1.wheels=9
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

Car.wheels=10

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)