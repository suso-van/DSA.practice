class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        
        for num in range(a, b + 1):
            # Convert the number to a string to check its digits
            num_str = str(num)
            
            # If the number of unique digits matches the length of the string, 
            # all digits are unique.
            if len(set(num_str)) == len(num_str):
                count += 1
                
        return count
