class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        d = 0
        i = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                d += 1
            i += 1

        return d