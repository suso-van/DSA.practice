class node:
    def __init__(self, data):
        self.data = data
        self.next = None    
        
class InsertionSort:        
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort = InsertionSort()    
sorted_arr = insertion_sort.insertion_sort(arr)
print("Sorted array is:", sorted_arr)   