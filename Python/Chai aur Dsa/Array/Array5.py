from array import *

val = array('i', [1, 2, 3, 4, 5])

#typecode is used to find the type of array 
print(val.typecode)

#reverse() is used to reverse the array
val.reverse()

for i in range(0 , len(val)):
    print(val[i], end=' ')
    
print("\n")
    
#insert() is used to insert a value at a particular index
val.insert(2, 10)

for i in range(0 , len(val)):
    print(val[i], end=' ')
    
print("\n")

#append() is used to add a value at the end of the array

val.append(20)

for i in range(0 , len(val)):
    print(val[i], end=' ')
    
print("\n")

#copy() is used to copy the array or we can also use list comprehension to copy the array

copyarray = array(val.typecode, ( x*2  for x in val))

for i in range(0 , len(val)):
    print(copyarray[i], end=' ')
    
print("\n")

#pop() is used to remove a value at a particular index

copyarray.pop(3)

for i in range(0 , len(copyarray)):
    print(copyarray[i], end=' ')
    
print("\n") 

# remove() is used to remove a value from the array

copyarray.remove(20)

for i in range(0 , len(copyarray)):
    print(copyarray[i], end=' ')
    

    