class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i, len(prices)):
                curr_profit = prices[j] - prices[i] if prices[j] - prices[i] > 0 else 0
                profit = max(profit, curr_profit)
        
        return profit