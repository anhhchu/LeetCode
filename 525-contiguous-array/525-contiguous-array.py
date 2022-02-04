class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        hm = {0:-1} # count : index
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in hm: 
                ans = max(ans, i - hm[count])
            else:
                hm[count] = i
                
        return ans