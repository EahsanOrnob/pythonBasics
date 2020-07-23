from numpy import *
multiarr = array([1, 3, 6, 73, 2])

print(multiarr)

#nothing to add

vals = linspace(0, 16, 17)
print(vals)

vals = logspace(0, 16, 17)
print(vals)
print('%2.2f' % vals[1])

arr = arange(0, 19, 2)
print(arr)

multiarr = array([1, 3, 6, 73, 2], float)
print(multiarr.dtype)
print(multiarr)

arr = zeros(5)
print(arr)

arr = ones(5, int)
print(arr)