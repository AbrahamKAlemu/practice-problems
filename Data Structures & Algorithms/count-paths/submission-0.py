class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [1] * m
        for i in range(n - 1):
            temp = path[::]
            for j in range(len(temp) - 2, -1, -1):
                temp[j] = temp[j + 1] + path[j]
            path = temp
        return path[0]
        