class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dfs(r, c, prev):
            if (r < 0 or r == len(matrix) or
                    c < 0 or c == len(matrix[r]) or 
                    matrix[r][c] <= prev):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            cache[(r, c)] = res

            return res
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) not in cache:
                    res = max(res, dfs(i, j, -1))

        return res