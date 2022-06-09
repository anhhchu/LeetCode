class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[0] = dp[-2] + nums[0] = dp[0] = 1
        dp[1] = dp[-1] + nums[1] = dp[1] = 2
        dp[2] = dp[0] + nums[2] = 1 + 3 = 4
        dp[3] = dp[1] + nums[3] = 2 + 1 = 3
        
        dp[i]: max profit to rob up to and including house i
        
        """
        def dp(i):
            if i < 0 or i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + dp(i-2), dp(i-1))
            return memo[i]
        
        memo = {}
        return dp(len(nums)-1)
        