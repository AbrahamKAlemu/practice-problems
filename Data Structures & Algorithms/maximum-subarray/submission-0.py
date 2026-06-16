class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if res >= 0:
                temp = max(0, temp + n)
            else:
                temp = max(temp, n)
            res = max(res, temp)
        return res
        