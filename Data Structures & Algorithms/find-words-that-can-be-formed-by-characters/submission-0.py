from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            word_count = Counter(word)
            valid = True
            for c in word:
                if c not in count or word_count[c] > count[c]:
                    valid = False
                    break
            if valid:
                res += len(word)
        return res 

        