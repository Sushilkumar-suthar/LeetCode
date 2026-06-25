class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            distance = target-n
            if distance in d:
                return (d[distance],i)
            else:
                d[n] = i