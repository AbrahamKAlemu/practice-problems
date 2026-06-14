class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for j in range(len(word1) + 1)]
        n = len(word1)
        m = len(word2)
        for i in range(n + 1):
            dp[i][m] = n - i
        for i in range(m + 1):
            dp[n][i] = m - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]) 
        return dp[0][0]

        