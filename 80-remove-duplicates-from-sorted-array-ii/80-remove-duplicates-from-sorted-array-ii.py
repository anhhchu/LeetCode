from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        0  1 2 3 4 5 6 7 8
        [0,0,1,1,1,1,2,3,3]
        i   j   hm   
        0   0   [0:1]
        1   1   [0:2]
        2   2   [0:2, 1:1]
        3   3   [0:2, 1:2]
        4   4   [0:2, 1:2] -> nums[i] == nums[j], hm[nums[j]] == 2, inc j
        4   5   [0:2, 1:2] -> nums[i] == nums[j], hm[nums[j]] == 2, inc j
        4   6   [0:2, 1:2, 2:1] -> set nums[i] = nums[j]
        
        
        => return sum(hm.values())
        
        """
        
        hm = defaultdict(int)
        i, j = 0, 0
        while j < len(nums):
            if nums[j] not in hm or (hm[nums[j]] < 2):
                nums[i] = nums[j]
                hm[nums[j]] += 1
                i += 1
                j += 1
            #elif nums[i] == nums[j] and hm[nums[j]] == 2:
            else:
                j += 1
                
        #print(hm)
        return sum(hm.values())
                
                        
        