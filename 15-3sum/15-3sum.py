class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -2 0 0 0 0 0 2 3
        """
        # first sort the list so we can call 2 sum
        nums.sort()
        output = []
        
        def twoSum(l, r, target):
            start = l 
            while l < r:
                if nums[l] + nums[r] == target: 
                    if l == start or (l > start and nums[l-1] != nums[l]): 
                        output.append([-target, nums[l], nums[r]])
                        r -= 1
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1 
            return
        
        
        for i, num in enumerate(nums):
            # call 2sum on the remaining list to find val1 + val2 = -num
            # skip duplicate value
            if i == 0 or (i > 0 and nums[i-1] != num): 
                twoSum(i + 1, len(nums) - 1, -num)
        
        return output
            
                    
                
            
        