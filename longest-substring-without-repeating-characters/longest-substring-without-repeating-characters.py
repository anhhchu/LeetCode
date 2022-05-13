class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
         s  e
        "abcabcbb"
        
        {a:3, b:1, c:2}
        
        """
        
        start = end = 0
        longest = 0
        hm = {}
        while end < len(s):
            if s[end] in hm:
                start = max(start, hm[s[end]] + 1)
               
            hm[s[end]] = end
            longest = max(longest, end-start+1)
            end += 1
            
        return longest
            