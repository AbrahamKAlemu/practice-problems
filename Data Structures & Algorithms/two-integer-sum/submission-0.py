class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            if n in complement:
                return [complement[n], i]
            else:
                complement[target - n] = i