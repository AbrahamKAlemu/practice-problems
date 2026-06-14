class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = (str(x)[::-1])
            n = "-" + n[:len(n) - 1]
        else:
            n = str(x)[::-1]
        
        x = int(n)
        if x > (2 ** 31) - 1 or x < (-2) ** 31:
            return 0
        return int(n)
