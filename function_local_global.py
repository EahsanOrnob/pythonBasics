# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 01:23:35 2020

@author: User
"""

"""
a=10

def localvari():
    a=8
    print("inside", a)
localvari()
print("outside",a)


a=10

def localvari():
   
    print("inside", a)
localvari()
print("outside",a)


a=10

def localvari():
    global a
    a=8
    print("inside", a)
localvari()
print("outside",a)
"""

a=10

def localvari():
    globals()['a']=15
    a=8
    print("inside", a)
localvari()
print("outside",a)