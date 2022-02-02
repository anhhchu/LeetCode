class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        if x % 10 == 0 and x != 0:
            return False
        
        firstHalf = 0
        while x > firstHalf: # 12,12
            firstHalf = firstHalf * 10 + x % 10 # 10 + 2 = 12
            x //= 10 
        
        return x == firstHalf or x == firstHalf//10 
        
        