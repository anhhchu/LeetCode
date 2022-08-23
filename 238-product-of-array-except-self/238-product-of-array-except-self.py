class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        # prefix: product of number up to and include i
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        # postfix: product of number from i to the right
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        for i in range(len(nums)):
            left = 1 if i == 0 else prefix[i - 1]
            right = 1 if i == len(nums) - 1 else postfix[i + 1]
            output[i] = left * right
            
        return output