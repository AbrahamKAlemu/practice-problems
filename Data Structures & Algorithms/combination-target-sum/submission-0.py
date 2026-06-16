class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(i, tot):
            if target == tot:
                res.append(temp[::])
                return
            if i == len(nums) or tot > target:
                return
            
            temp.append(nums[i])
            dfs(i, tot + nums[i])
            temp.pop()
            dfs(i + 1, tot)
            return
        dfs(0, 0)
        return res


        