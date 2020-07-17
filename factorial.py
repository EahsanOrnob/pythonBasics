# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:40:02 2020

@author: User
"""


def fect(n):
    f=1
    for i in range(1,n+1):
        c= f*i
        f= c
    print(c)
        
fect(5)

def fector(n):
    if n==0:
        return 1
    j=n*fector(n-1)    
    return j
    
x=fector(5)
print(x)

