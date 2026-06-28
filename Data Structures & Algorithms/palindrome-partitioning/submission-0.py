class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        temp = []

        def isPal(strs):
            l, r = 0, len(strs) - 1
            while l < r:
                if strs[l] != strs[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(temp[::])
                return
            for j in range(i + 1, len(s) + 1):
                if isPal(s[i : j]):
                    temp.append(s[i: j])
                    dfs(j)
                    temp.pop()


        dfs(0)
        return res
                