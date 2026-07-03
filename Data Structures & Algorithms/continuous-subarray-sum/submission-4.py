class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder = {0 : -1}
        val = 0

        for i, num in enumerate(nums):
            val += num
            rem = val % k
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] > 1:
                return True
        
        return False
            
        