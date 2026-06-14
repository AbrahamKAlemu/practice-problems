class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        offset = 31
        while n != 0:
            res += (n & 1) * (2 ** offset)
            n >>= 1
            offset -= 1
        return res
        