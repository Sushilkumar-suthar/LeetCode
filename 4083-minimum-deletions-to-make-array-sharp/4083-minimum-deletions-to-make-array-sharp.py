class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        return sum([1 for i in range(len(nums)-1) if nums[i] == nums[i+1]])