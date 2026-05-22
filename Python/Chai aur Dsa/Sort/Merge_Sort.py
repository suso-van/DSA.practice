class node:
    def __init__(self, data):
        self.data = data
        self.next = None    

class MergeSort:    
    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        
        return self.merge(left_half, right_half)
    
# Example usage:    
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort = MergeSort()
sorted_arr = merge_sort.merge_sort(arr)
print("Sorted array is:", sorted_arr)   
