class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                unique = len(seen)
                total += unique * unique

        return total