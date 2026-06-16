class Solution:
    def numDecodings(self, s: str) -> int:
        next1, next2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cur = 0
            else:
                cur = next1 
                if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and 
                        s[i + 1] in "0123456")):
                    cur += next2
            next1, next2 = cur, next1
        return next1 if s[0] != "0" else 0
