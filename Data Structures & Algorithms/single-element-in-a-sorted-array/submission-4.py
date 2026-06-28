class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(m)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and
                    (m == len(nums) - 1 or nums[m + 1] != nums[m])):
                return nums[m]
            left_size = 0
            if (m != 0 and nums[m - 1] == nums[m]):
                left_size = m - 1
            else:
                left_size = m

            if left_size % 2 == 0:
                l = m + 1
            else:
                r = m - 1
        return -1

        