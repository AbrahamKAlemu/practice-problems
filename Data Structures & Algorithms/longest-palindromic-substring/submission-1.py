class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def pal(l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return False
            return True
        
        res = ""

        for i in range(len(s)):
            l, r = i, i + 1
            while pal(l, r):
                if r - l + 1 > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
            
            l, r = i, i
            while pal(l, r):
                if r - l + 1 > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
        return res

            