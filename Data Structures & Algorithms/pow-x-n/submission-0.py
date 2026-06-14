class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(i):
            if i == 0:
                return 1
            if i == 1:
                return x
            
            return dfs(i // 2) * dfs((i // 2) + (i % 2)) 
        return dfs(abs(n)) if n >= 0 else 1 / dfs(abs(n))