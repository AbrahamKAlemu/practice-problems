class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cur, prev = 2, 1
        for i in range(3, n + 1):
            cur, prev = cur + prev, cur
        return cur
        