class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]
        for val in nums:
            temp = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm = perm[: i] + [val] + perm[i:]
                    temp.append(new_perm)
            perms = temp

        return perms
        