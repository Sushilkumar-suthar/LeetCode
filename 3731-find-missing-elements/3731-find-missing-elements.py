class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = min(nums)
        h = max(nums)
        return [i for i in range(l,h+1) if i not in nums]