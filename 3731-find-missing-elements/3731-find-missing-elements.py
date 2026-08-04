class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = min(nums)
        h = max(nums)
        nl = [i for i in range(l,h+1) if i not in nums]
        return nl