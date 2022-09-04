class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -2 0 0 0 0 0 1 1 2 3
        """
        # first sort the list so we can call 2 sum
        nums.sort()
        output = []
        
        
        for i, num in enumerate(nums):
            # binary search in list nums[i+1:]
            # skip duplicate value
            if i == 0 or (i > 0 and nums[i-1] != num): 
                l, r = i+1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < -nums[i]:
                        l += 1
                    elif nums[l] + nums[r] > -nums[i]:
                        r -= 1
                    elif nums[l] + nums[r] == -nums[i]:
                        # add to output
                        output.append([nums[i], nums[l], nums[r]])
                        l += 1
                        # skip duplicate value
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        r -= 1
        return output
            
                    
                
            
        