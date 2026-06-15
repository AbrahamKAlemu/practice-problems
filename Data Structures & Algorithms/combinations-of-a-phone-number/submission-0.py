class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2" : "abc", "3" : "def", "4" : "ghi", 
                        "5" : "jkl", "6" : "mno", "7" : "pqrs", 
                        "8" : "tuv", "9" : "wxyz"}
        
        res = [""]
        for c in digits:
            temp = []
            for d in mapping[c]:
                for com in res:
                    temp.append(com + d)
            res = temp
        return res if digits != "" else []
        