# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:50:47 2020

@author: User
"""

class Computer:
    def __init__(self,cpu,ram):
         #print("in init")
        self.cpu=cpu
        self.ram=ram
    
    def config(self):
         print("config is",self.cpu, self.ram)
 
#constractor/Computer('i5',16)
com1=Computer('i5',16)
com2=Computer('Ryzen3',8)
#print(type(com1))
"""
Computer.config(com1)
Computer.config(com2)
"""
com1.config()
com2.config() 