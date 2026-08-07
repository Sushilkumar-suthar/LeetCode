class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:return False
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True

        return False