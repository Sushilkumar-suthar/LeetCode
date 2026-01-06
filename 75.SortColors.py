class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Terms: Do not return anything, modify nums in-place instead.
        Result: Accepted
        Beats: 100% at 0ms
        Memory: 19.42MB Beats: 8%
        """
        index = 0
        i = 0
        last_pointer= len(nums)
        while index<len(nums) and last_pointer!=index:
            i=index
            if nums[i]==0:
                index+=1
                nums.pop(i)
                nums.insert(0,0)
            elif nums[i]==1:
                nums.pop(i)
                nums.insert(index,1)
                index+=1
            else:
                nums.pop(i)
                nums.append(2)
                last_pointer-=1
        