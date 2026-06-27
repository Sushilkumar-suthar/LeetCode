class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = -float('inf')
        s = -float('inf')
        t = -float('inf')
        if len(set(nums))<=2: 
            return max(nums)
        for i in nums:
            if i>f:
                t = s
                s= f
                f=i
            elif i>s and i!=f:
                t = s
                s = i
            elif i>t and i!=f  and i!=s:t=i
        return t