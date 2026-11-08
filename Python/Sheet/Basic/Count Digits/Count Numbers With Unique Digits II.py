class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        
        for num in range(a, b + 1):
            num_str = str(num)
            if len(set(num_str)) == len(num_str):
                count += 1
                
        return count
