from numpy import *

#numpy is a library in python which is used to work with arrays and matrices. It also has a lot of functions to work with these arrays.

val = array([1, 2, 3, 4, 5])

for x in val:
    print(x , end=' ')
    
print("\n")
# we can also create an array of float type
    
val2 = array([6, 7, 8, 9, 10], float)

for x in val2:
    print(x , end=' ')
    
print("\n")

val = linspace(0, 10, 5) 

# it is used to create an array of equally spaced values between a given range. Here it will create an array of 5 values between 0 and 10.

for x in val:
    print(x , end=' ')
    
print("\n")

#arange() is used to create an array of values between a given range with a given step. Here it will create an array of values between 0 and 10 with a step of 2.

val = arange(0, 10, 2)

for x in val:
    print(x , end=' ')
    
print("\n") 

#logspace() is used to create an array of values between a given range with a given number of values. Here it will create an array of 5 values between 10^0 and 10^2.   

val = logspace(0, 2, 5)

for x in val:
    print(x , end=' ')
    
print("\n")

#zeros() is used to create an array of zeros with a given shape. Here it will create an array of 5 zeros.   

val = zeros(5)

for x in val:
    print(x , end=' ')      
    
print("\n")

#ones() is used to create an array of ones with a given shape. Here it will create an array of 5 ones.  

val = ones(5)

for x in val:
    print(x , end=' ')
    
print("\n")

#eye() is used to create an identity matrix of a given size. Here it will create an identity matrix of size 3x3.

val = eye(3)

for x in val:
    print(x , end=' ')
    
print("\n")

#diag() is used to create a diagonal matrix with a given array. Here it will create a diagonal matrix with the given array.

val = diag([1, 2, 3])

for x in val:
    print(x , end=' ')
    
print("\n")

#full() is used to create an array of a given shape and fill it with a given value. Here it will create an array of shape 3x3 and fill it with the value 5.

val = full((3, 3), 5)

for x in val:
    print(x , end=' ')
    
print("\n")

#multidimensional arrays can also be created using the array() function. Here it will create a 2D array of shape 3x3.   

zero = array(10)
print(zero)
print("\n")

one = array([1, 1, 1, 1, 1])
print(one)
print("\n")

two = array([[1,2,3], [4,5,6], [7,8,9]])
print(two)
print("\n")

three = array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]], [[19,20,21], [22,23,24], [25,26,27]]])
print(three)
print("\n")

