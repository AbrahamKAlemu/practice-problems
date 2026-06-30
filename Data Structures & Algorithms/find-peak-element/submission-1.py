class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m - 1
            elif nums[m] > nums[m - 1]:
                l = m + 1
            else:
                r = m - 1
        return 0
        
        