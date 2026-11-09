class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)

        for i in range(hl-nl+1):
            if haystack[i:i+nl]==needle:
                return i

        return -1