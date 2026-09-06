class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                elif skipS:
                    skipS -= 1
                else:
                    break
                i -= 1

            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                elif skipT:
                    skipT -= 1
                else:
                    break
                j -= 1

            if i < 0 or j < 0:
                return i == j

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True