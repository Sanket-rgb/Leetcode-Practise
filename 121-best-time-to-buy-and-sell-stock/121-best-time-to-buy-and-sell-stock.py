class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
#         maxProfit = 0
        
#         for i in range(len(prices)):
#             diff = self.difference(prices[i], prices[i:])
            
#             if diff > maxProfit:
#                 maxProfit = diff
#         return maxProfit
        
        
#     def difference(self, n, arr):
#         return max(arr) - n
        