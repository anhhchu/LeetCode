class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = 0
        max_prices = [0 for _ in range(len(prices))]
        # 6, 6, 6, 6, 4, 0
        # find the max price to the right of i
        for i in range(len(prices) - 2, -1, -1):
            max_prices[i] = max(max_right, prices[i+1])
            max_right = max(max_right, prices[i+1])
 
        max_price = 0
        for i in range(len(prices)):
            max_price = max(max_prices[i] - prices[i], max_price)
            
        return max_price