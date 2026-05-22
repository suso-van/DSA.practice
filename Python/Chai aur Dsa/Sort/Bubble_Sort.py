class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class BubbleSort:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort()
sorted_arr = bubble_sort.bubble_sort(arr)
print("Sorted array is:", sorted_arr)   