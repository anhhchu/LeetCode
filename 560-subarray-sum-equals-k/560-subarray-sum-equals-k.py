class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [-1,-2,3,3,6]
        k = 3
        hm = {0:1}
        i   sum   hm                s-k        hm
        0   -1    {0:1}             -1-3 = -4   {0:1, -1:1}
        1   -3    {0:1, -1,1}       -3-3 = -6   {0:1, -1:1, -3:1}
        2   0     {0:1, -1:1, -3:1} 0-3 = -3    {0:2, -1:1, -3:1} -> count = 1 as -3 is in hm
        3   3    {0:2, -1:1, -3:1}  3-3 = 0     {0:2, -1:1, -3:1, 3:1} -> count = 3 as 0 is in hm  
        4   9    {0:2, -1:1, -3:1, 3:1} 9-3 = 6 {0:2, -1:1, -3:1, 3:1, 9:1}
        
        => count = 3
        """
        hm = {0:1}
        s, count = 0, 0
        for num in nums:
            s += num
            if s - k in hm:
                count += hm[s-k]
            hm[s] = hm.get(s, 0) + 1
            
        return count
                
            