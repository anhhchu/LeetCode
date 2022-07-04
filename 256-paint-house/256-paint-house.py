class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        0   1   2
        ---------
        17  2   17
        16  16  5
        14  3   19
        
        
        use bottom up approach with matrix housexcolor time and space complexity
        at each cell, the cost of the house painted by that color + min(cost of prev house painted by a diff color)
        
        0   1   2
        ---------
        17  2   17
        18  33  7
        21  10  37 -> return min cost of last row
        
        
        """
        houses, colors = len(costs), len(costs[0])
           
        dp = [[0]*colors for _ in range(houses)]
        #print(dp)
        
        dp[0] = costs[0]
        #print(dp)
        
        for house in range(1, houses):
            for col in range(colors):
                # exclude current color
                prev_cost = min(dp[house-1][:col] + dp[house-1][col+1:])
                dp[house][col] = prev_cost + costs[house][col]
            
        #print(dp)
        return min(dp[houses-1])
        