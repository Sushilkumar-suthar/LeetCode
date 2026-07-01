class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        right = sum(nums)

        for i in range(len(nums)):
            right = sum(nums[i+1:])
            if left == right:
                return i
            left += nums[i]
        return -1