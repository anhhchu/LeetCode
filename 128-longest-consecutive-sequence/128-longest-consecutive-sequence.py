class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the first number of the sequence
        # construct the sequences
        
        nums_set = set(nums) # O(n)
        res = 0
        for num in nums: # O(n)
            length = 0
            if num-1 not in nums_set:
                # add the sequence first number to sequences
                length += 1
                nxt = num + 1
                while nxt in nums_set:
                    length+=1 
                    nxt += 1                    
            else:
                continue
            res = max(res, length)
        
        return res

            
                    

            
        