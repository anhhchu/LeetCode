class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        hm = {0:-1} # count : index
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in hm: 
                ans = max(ans, i - hm[count])
            else:
                hm[count] = i
                
        return ans