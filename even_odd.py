# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 01:42:28 2020

@author: User
"""


def count(l):
    
    even=0
    odd=0
    
    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1
            
    return even,odd

lst=[22,34,54,6,1,3,3,57,89,1]

e,o=count(lst)

print("Even : {} and Odd : {}".format (e,o))