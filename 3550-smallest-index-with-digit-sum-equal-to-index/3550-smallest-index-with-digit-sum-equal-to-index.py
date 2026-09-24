class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum = 0
            n = nums[i]
            while(n>0):
                sum+= (n%10)
                n = n//10
            if i==sum:return sum
        return -1