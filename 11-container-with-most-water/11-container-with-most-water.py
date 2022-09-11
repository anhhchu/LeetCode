class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set 2 pointers
        # compare height at L and R
        # calc the area height*(R-L) and record the max area
        # move the pointer of smaller height
        L, R = 0, len(height)-1
        res = 0
        while L < R:
            h = min(height[L], height[R])
            res = max(res, h*(R-L))
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
                
        return res
            
            
        