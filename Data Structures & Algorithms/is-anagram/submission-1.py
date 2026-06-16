from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC = Counter(s)
        tC = Counter(t)

        for key in sC:
            if sC[key] != tC[key]:
                return False
        for key in tC:
            if sC[key] != tC[key]:
                return False
        return True