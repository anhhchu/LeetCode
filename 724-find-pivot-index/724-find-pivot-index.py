class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 2:
        #     return 0
        
        """
        0 1 2 3
        1,2,0,3
        
        i = 0
        leftSum = 0, 
        rightSum = 6-1 = 5 
        
        i = 1 -> left = 0 + nums[:i-1] = 1, 
            right = 5 - nums[i] = 5 - 2 =3 
        i = 2 -> left = left + nums[i-1] = 1 + 2 = 3
            right = right - nums[i] = 3-0 = 0
            
        -> return 2
        
        """
        
        leftSum, rightSum = 0, sum(nums)-nums[0]
        if leftSum == rightSum:
            return 0
        
        for i in range(1, len(nums)):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        
        return -1 
            
            