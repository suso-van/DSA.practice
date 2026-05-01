import array

val = array.array('i', [1, 2, 3, 4, 5])

for i in range(0,5):
    print(val[i] , end=' ')
    
print("\n")
    
# or

for i in val:
    print(i , end=' , ')