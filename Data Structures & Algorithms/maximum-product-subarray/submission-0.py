class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal, maxVal = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            var = (minVal * nums[i], maxVal * nums[i], nums[i])
            minVal, maxVal = min(var), max(var)
            res = max(res, maxVal)
        return res



        