class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        srS, srT = sorted(s.lower()), sorted(t.lower())
        if srT == srS:
            return True
        else:
            return False
        