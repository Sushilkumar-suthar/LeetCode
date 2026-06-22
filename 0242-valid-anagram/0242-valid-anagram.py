class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        return list(sorted(s)) == list(sorted(t))