class Solution:
    def finalString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == "i" or i=="I":stack = stack[::-1]
            else:stack.append(i)

        return "".join(stack)