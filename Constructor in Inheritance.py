# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:17:49 2020

@author: User
"""


class A:
    def __init__(self):
        print("print from initA")
    
    def function1(self):
        print("this is printing Function1A")
    def function2(self):
        print("this is printing Function2")
#class B(A):
class B:
    def __init__(self):
        #super().__init__()
        print("print from initB")
    def function1(self):
        print("this is printing Function1B")
    def function4(self):
        print("this is printing Function4")
        

class C(A,B):
    def __init__(self):
        super().__init__()   #print always left to right
        print("print from initC")  

    def func(self):
        super().function4()

c1=A()
c2=B()
c3=C()
c3.function1()     #print always left to right
c3.func()
