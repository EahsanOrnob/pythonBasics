# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:38:01 2020

@author: User
"""
"""

def corona():
    print('Kill you')
    
def add(x,y):
    c=x+y
    return c

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d


corona()
result= add(5,6)
print(result)

result1,result2=add_sub(6,7)

print(result1,result2)

def update(x):
    print(id(x))
    x=9
    print(id(x))
    return x


n=10
print(id(n))
result33=update(n)
print(result33)



def update(x):
    print(id(x))
    x[1]=9
    print(id(x))
    return x


n=[10,20,50]
print(id(n))
result33=update(n)
print(result33)



def person(name, age):
    print(name)
    print(age-2)
    
person('ornob',22)  
person(age=22 ,name='ornob')



def sum(a,b):
    c=a+b
    print(c)
    
sum(5,6)

#tuple 
def sum(a,*b):
    c=a
    
    for i in b:
        c=c+i
       
    print(c)
    
sum(5,6,7,8,9,3)

#tuple 

def sum(*b):
    c=0
    
    for i in b:
        c=c+i
    print(c)
    
sum(5,6,7,8,9,3)



#keyword variable length argument


def person(name,*data):
    print(name)
    print(data)
    
person('ornob', 22, 'Dhaka', '01647' )

def person(name,**data):
    print(name)
    print(data)
    
person('ornob', age=22, city='Dhaka', mob=1647 )  
  

def person(name,**data):
    print(name)
    
    for i,j in data.items():
        print(i,j)
    
person('ornob', age=22, city='Dhaka', mob=1647 )  

def person(**data):
   
    for i,j in data.items():
        print(i,j)
    
person(name='ornob', age=22, city='Dhaka', mob=1647 ) 
  """
