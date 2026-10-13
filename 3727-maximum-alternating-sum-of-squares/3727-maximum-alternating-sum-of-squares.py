class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort()

        ans = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            ans += nums[right] - nums[left]
            left += 1
            right -= 1

        if left == right:
            ans += nums[left]

        return ans