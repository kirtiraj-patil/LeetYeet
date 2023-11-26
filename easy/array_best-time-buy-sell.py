class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currentMax = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > currentMax:
                currentMax = prices[i]
            elif currentMax - prices[i] > profit:
                profit = currentMax - prices[i]

        return profit
