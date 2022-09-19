class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """ sliding window
        start, end = 0
        distinct = {e:2 c:1} -> keep track of char:last_index
        max_length = 0
        while end < len(s): 
            char = s[end]
            if distinct length < 2: 
                add to distinct -> char:index
                incr end
            else:  
                if char in distinct:
                    update last_index of char in distinct
                    incr end 
                elif char not in distinct: 
                    keep char with higher last index , replace the other one with the new char
                    start = index of the replaced char + 1
                    incr end
                    
            max_length = max(end - start, max_length)
        
        
        
        start   end     char
        0   0   e   -> {e:0} -> max_length = 1
        0   1   c   -> {e:0, c:1} -> max_length = 2
        0   2   e   -> {e:2, c:1} -> max_length = 3
        0   3   b   -> {e:2, b:3} -> start = 2, end = 4 -> max_length = 3
        2   4   a   -> {b:3, a:4} -> start = 3, end = 5 -> max_length = 3
         
        """
        start = end = 0
        max_len = 0
        distinct = {} # key is char, last_index is value
        
        while end < len(s):
            char = s[end]
            if len(distinct) < 2 or char in distinct:
                distinct[char] = end
                
            elif len(distinct) == 2 and char not in distinct:
                # find char with smaller index
                replaced_char = min(distinct, key = distinct.get)
                smaller_index = distinct[replaced_char]
                # replace with new char
                distinct.pop(replaced_char)
                distinct[char] = end
                start = smaller_index + 1
                
            end += 1
            max_len = max(max_len, end - start)
            
            
        return max_len
                
                
                
            
            
            
            