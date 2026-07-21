class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                maxi = mini = 1
                continue
            maxi, mini = max(maxi * n, mini * n, n), min(maxi * n, mini * n, n)
            res = max(res, maxi)
        return res
        
        