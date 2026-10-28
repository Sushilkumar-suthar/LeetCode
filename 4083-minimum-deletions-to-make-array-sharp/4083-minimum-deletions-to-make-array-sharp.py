class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        d = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                d += 1
        return d