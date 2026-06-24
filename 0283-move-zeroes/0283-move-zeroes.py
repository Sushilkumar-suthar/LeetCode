class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        l = len(nums)
        for i in range(len(nums)):
            if nums[p]==0:nums.append(nums.pop(p))
            else:p+=1
            if p>=l:break