class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        count = Counter(words[0])
        for word in words:
            wC = Counter(word)
            for c in count:
                if count[c] > wC[c]:
                    count[c] = wC[c]
                print(count)
        for key in count:
            for i in range(count[key]):
                res.append(key)
        return res 
        