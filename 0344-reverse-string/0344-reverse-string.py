class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        last = len(s)-1
        while start<last:
            s[start],s[last] = s[last],s[start]
            start+=1
            last-=1