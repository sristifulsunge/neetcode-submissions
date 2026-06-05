class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #using two pointer method 
        min_buy = float('inf')
        max_sell = 0
        max_profit = 0

        for price in prices:
            if price < min_buy:
                min_buy = price
            profit = price - min_buy
            max_profit = max(max_profit, profit)

        return max_profit