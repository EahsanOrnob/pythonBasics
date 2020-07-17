# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:53:26 2020

@author: User
"""

def div(a,b):
    print(a/b)
    
def smart_div(func):
    
    def inside1(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    
    return inside1
 
div1=smart_div(div)   

div1(3,5)
