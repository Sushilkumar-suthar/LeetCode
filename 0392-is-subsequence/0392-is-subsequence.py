class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:return True
        p = 0
        for c in t:
            if s[p] ==c:
                p+=1
                if p==len(s):return True
        return False