class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        stack = []
        d ={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                p = stack.pop()

                if not p == d[i]:
                    return False

        return len(stack)==0