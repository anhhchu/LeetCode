class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
                [],[1,1,2]
        [1][1,2]        [2][1,1]
    [1,1][2]   [1,2][1]     [2,1][1]
[1,1,2][]      [1,2,1][]    [2,1,1][]
                
  
        """
        output = []
        nums.sort()
        def _permute(res, rem):
            # res: result of each step
            # rem: remaining list in sorted order
            if len(rem) == 0:
                output.append(res)
                return
            i = 0
            while i < len(rem):
                if i-1 < 0 or rem[i] != rem[i-1]:
                    _permute(res+[rem[i]], rem[:i]+rem[i+1:])
                i += 1
                
        _permute([], nums)
        
        
        return output
                    