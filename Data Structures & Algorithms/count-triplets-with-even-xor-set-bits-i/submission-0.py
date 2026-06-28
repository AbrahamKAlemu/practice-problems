class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        tab = 0
        for i in a:
            for j in b:
                for k in c:
                    val = i ^ j ^ k
                    if val.bit_count() % 2 == 0:
                        tab += 1
        return tab