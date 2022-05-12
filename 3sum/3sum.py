class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        for each num x:
            search for 2 nums that add up to target = -x use 2 pointers (i, j) with the rest of the array
            * if y+z > target, j-1
            * if y+z < target, i+1
            * if y+z == target, i+1 and j-1
            
        x = -4 -> search for y+z = 4 
                     i j
            [-1,-1,0,1,2]
        
        
        x = -1 -> search for y+z = 1
                i j
            [-1,0,1,2] => Found (-1,-1,2), (-1,0,1)

        x = -1 (skip)
        
        x = 0 -> search for y+z = 0
             i j  
            [1,2] 
        
        """
        def _twoSum(i, j, target):
            #print(target)
            while i < j:
                if nums[i] + nums[j] == target:
                    res = [-target, nums[i], nums[j]]
                    if res not in output: output.append(res)
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                
        
        nums.sort()
        output = []
        n = len(nums)-1
        #print(nums)
        
        for i, x in enumerate(nums):
            if i == 0 or x != nums[i-1]:
                _twoSum(i+1, n, -x)
            
        return output
        
        