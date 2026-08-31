class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        count = 0
        if len(s)==0:return 0
        for i in s:
            if i=='R':c+=1
            else:
                c-=1
            if c==0:count+=1
        return count