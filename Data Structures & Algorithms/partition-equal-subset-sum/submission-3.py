class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2:
            return False
        
        cache = {}
        def dfs(i, tot):
            if (i, tot) in cache:
                return cache[(i, tot)]
            if tot == target:
                cache[(i, tot)] = True
                return True
            if tot > target or i >= len(nums):
                cache[(i, tot)] = False
                return False
            cache[(i, tot)] = dfs(i + 1, tot) or dfs(i + 1, tot + nums[i])
            return cache[(i, tot)]
        
        return dfs(0, 0)
        