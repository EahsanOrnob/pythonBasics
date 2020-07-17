# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:34:58 2020

@author: User
"""

class Computer:
    def __init__(self):
        self.name='Ornob'
        self.age=23
    
    def update(self):
        self.age=30
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
    
c1=Computer()
c2=Computer()

#c1.name="Rashai"
#c1.age=12

#print(c1.name,c1.age)

#c1.update()

print(c1.name,c1.age)
print(c2.name,c2.age)

if c1.compare(c2):
    print("They are same")
    
else:
    print("They are different")

#print(id(c1))
#print(id(c2))