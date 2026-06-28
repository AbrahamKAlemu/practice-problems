class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def dfs(i, c):
            if (i, c) in cache:
                return cache[(i, c)]
            if i >= len(cost):
                return c
            
            cache[(i, c)] = min(dfs(i + 1, c + cost[i]), dfs(i + 2, c + cost[i]))
            return cache[(i, c)]
        return min(dfs(0, 0), dfs(1, 0))
        