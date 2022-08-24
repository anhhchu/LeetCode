class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the first number of the sequence
        # construct the sequences
        sequences = {} # dict of first number and length of the sequence
        nums_set = set(nums) # O(n)
        res = 0
        for num in nums: # O(n)
            if num-1 not in nums_set:
                # add the sequence first number to sequences
                sequences[num] = 1
                nxt = num + 1
                while nxt in nums_set:
                    sequences[num]+=1 
                    nxt += 1                    
            else:
                continue
            res = max(res, sequences[num])
        
        return res

            
                    

            
        