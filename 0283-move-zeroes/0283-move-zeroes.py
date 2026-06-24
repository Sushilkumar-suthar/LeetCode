class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        f = 0
        while f<l:
            if nums[l] !=0 and nums[f]==0:
                nums.pop(f)
                nums.append(0)
                l-=1
            if nums[l]==0:l-=1
            if nums[f]!=0:f+=1