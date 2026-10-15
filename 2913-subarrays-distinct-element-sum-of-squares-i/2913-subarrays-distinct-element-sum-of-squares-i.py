class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                unique = len(set(nums[i:j+1]))
                sum += unique ** 2
        return sum