# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 01:18:33 2020

@author: User
"""

class A:
    def function1(self):
        print("this is printing Function1")
    def function2(self):
        print("this is printing Function2")
class B(A):
    def function3(self):
        print("this is printing Function3")
    def function4(self):
        print("this is printing Function4")
class C(B):
    def function5(self):
        print("this is printing Function5")

c1=A()
c2=B()
c3=C()


c1.function1()
c1.function2()

c2.function3()
c3.function1()
c3.function5()