# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import *

arr1= array([
    [1,2,3,4,9,3],
    [2,3,4,5,5,7]
    ])

m = matrix(arr1)

m = matrix('1 2 ; 2 3 ; 3 4')
print(m)


print(arr1)

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2= arr1.flatten()
print(arr2)

arr3=arr2.reshape(3,4)
print(arr3)


arr4=arr2.reshape(2,2,3)
print(arr4)
"""
arr1 = array([1,2,3,45,6,8,65,4])
arr2= array([13,2,3,45,6,8,65,4])


arr3=arr1.copy()
arr3[1]=7
print (id(arr1))
print (id(arr3))

print(arr3)
print(arr1)

print(concatenate([arr1, arr2]))

arr3=arr1*arr2
print(arr3)
print(cos(arr1))
print(sqrt(arr1))
arr4=sin(arr1)*sin(arr1)+cos(arr1)*cos(arr1)
print(arr4)

print(sum(arr1))
 """