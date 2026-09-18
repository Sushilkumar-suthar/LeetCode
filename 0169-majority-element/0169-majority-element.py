class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mx = 0
        mxc= 0
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
                if d[i]>mxc:
                    mxc=d[i]
                    mx=i
            else:
                d[i]+=1
                if d[i]>mxc:
                    mxc=d[i]
                    mx=i
        return mx 