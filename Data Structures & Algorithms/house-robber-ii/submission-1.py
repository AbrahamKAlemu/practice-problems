class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, cur = 0, 0
        for i in range(len(nums) - 1):
            prev, cur = cur, max(cur, prev + nums[i])
        res = cur

        prev, cur = 0, 0
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])
        res = max(res, cur)

        return res
