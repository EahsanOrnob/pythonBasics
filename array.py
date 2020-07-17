from array import *

vals= array('i',[1,-2,3])
print (vals)

vals= array('I',[1,2,3])
print (vals)

newvals= array(vals.typecode,  (a*a for a in vals))
print(newvals)

vals= array('i',[1,-2,3])
for i in range(3):
    print(vals[i])

vals= array('f',[1,2.5,3,1])
print (vals.count(1))

newarray= array('i', [])
n= int(input("enter the array range"))
for i in range(n):
    x = int(input("enter a value"))
    newarray.append(x)
print(newarray)

vals= array('u',['a','b','x'])
print (vals)

newvals= array(vals.typecode,  (a for a in vals))
print(newvals)