class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        temp = []
        candidates.sort()

        def dfs(i):
            if sum(temp) == target:
                res.append(temp[::])
                return
            if sum(temp) > target or i >= len(candidates):
                return

            
            temp.append(candidates[i])
            dfs(i + 1)
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)
            
        dfs(0)
        return res
        