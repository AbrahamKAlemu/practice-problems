class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        m = 1
        for i in range(1, n + 1):
            if m << 1  == i:
                m = i
                dp[i] = 1
            else:
                dp[i] = 1 + dp[i - m]
        return dp
        