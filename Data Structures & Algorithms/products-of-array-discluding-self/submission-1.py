class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        postfix = nums[:]
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] *= postfix[i + 1]
        
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1 
            right = postfix[i + 1] if i + 1 < len(nums) else 1
            nums[i] = left * right
        
        return nums
