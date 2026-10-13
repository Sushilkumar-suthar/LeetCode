class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        nums.sort()

        ans = 0
        left, right = 0, len(nums) - 1

        while left < right:
            ans += nums[right] - nums[left]
            left += 1
            right -= 1

        if left == right:
            ans += nums[left]

        return ans