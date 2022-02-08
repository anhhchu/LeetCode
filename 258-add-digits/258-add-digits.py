class Solution:
    def addDigits(self, num: int) -> int:
        digit_sums = 0
        while num > 0: # 38
            digit_sums += (num%10)
            num //= 10
            if num == 0 and digit_sums >= 10:
                num = digit_sums
                digit_sums = 0
            
        return digit_sums