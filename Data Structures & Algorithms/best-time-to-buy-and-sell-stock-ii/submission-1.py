class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """cache = {}
        def dfs(i, buy):
            if (i, buy) in cache:
                return cache[(i, buy)]
            if i == len(prices):
                cache[(i, buy)] = total
                return cache[(i, total, buy)]
            if buy:
                cache[(i, total, buy)] = max(dfs(i + 1, total - prices[i], not buy), 
                    dfs(i + 1, total, buy))
                return cache[(i, total, buy)] 
            else:
                cache[(i, total, buy)] = max(dfs(i + 1, total + prices[i], not buy), 
                    dfs(i + 1, total, buy))
                return cache[(i, total, buy)]
        return dfs(0, 0, True)"""

        price = 0
        for i in range(1, len(prices)):
            price += prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0
        return price


        