class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        cnt = 0

        while temp > 0:
            if num % (temp % 10) == 0:
                cnt += 1
            temp = temp // 10

        return cnt     