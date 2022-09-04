class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 2 pointers, check value of s[L], s[R] -> inc L, dec R
        # encounter the non-alpha char, change the pointer
        # L >= R -> return True
        # s[L] != s[R] val is alphanum -> return False and exit loop
        
        L, R = 0, len(s)-1
        while L < R:
            while L < R and (not s[L].isalnum()):
                L += 1
            while L < R and (not s[R].isalnum()):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
            
        return True