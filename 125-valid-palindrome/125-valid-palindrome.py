class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''.join([char.lower() for char in s if char.isalnum()]) # O(N)
        return new == new[::-1]
        