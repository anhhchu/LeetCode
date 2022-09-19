class Solution:
    def trap(self, height: List[int]) -> int:
        """
        0,1,0,2,1,0,1,3,2,1,2,1
        
        0,1,1,2,2,2,2,3,3,3,3,3
        3,3,3,3,3,3,3,3,2,2,2,1  
        
        """
        
        # min(max_left, max_right) - height
        total = 0
        
        max_left = []
        max_right = [0 for _ in range(len(height))]
        L, R = 0, 0
        
        for i in range(len(height)):
            max_left.append(max(L, height[i]))
            L = max(L, height[i])
            
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max(R, height[i])
            R = max(R, height[i])
        
        for i in range(len(height)):
            total += min(max_left[i], max_right[i]) - height[i]
            
        return total