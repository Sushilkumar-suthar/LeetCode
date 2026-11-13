class Solution:
    def finalString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == "i" or i=="I":
                stack = stack[::-1]
                # s.append(i)
            else:
                stack.append(i)

        return "".join(stack)