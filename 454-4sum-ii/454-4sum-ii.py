from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # O(N^2) time and space -> max iterations: 200**2 = 40000
        hm = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                hm[num1+num2] += 1
                
        ans = 0
        #print(hm)
        for num3 in nums3:
            for num4 in nums4:
                val = -(num3 + num4)
                if val in hm:
                    ans += hm[val]
                    
        return ans