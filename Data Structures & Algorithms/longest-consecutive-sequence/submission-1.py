class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        res = 1
        for n in nums:
            if n - 1 not in vals:
                c = 1
                for i in range(1, len(nums)):
                    if n + i in vals:
                        res = max(res, c + i)
                    else:
                        break
        return res if nums else 0