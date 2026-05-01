from array import *

arr = array('i', [])
# display the array before adding any element

n = int(input("Enter the number of elements you want to add in the array : "))

for i in range(0, n):
    arr.append(int(input("Enter the element : ")))

print("The elements in the array are : ")
for i in range(0, len(arr)):
    print(arr[i], end=' ')
    
print
  
# to find the index of an element in the array

val = array('i', [1, 2, 3, 4, 5])
  
j = val.index(3)
 
print("\nThe index of 3 is : ", j)