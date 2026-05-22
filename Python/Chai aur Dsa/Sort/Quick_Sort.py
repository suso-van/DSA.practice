class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)  

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort = QuickSort()
quick_sort.quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)