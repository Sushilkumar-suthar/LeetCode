class Solution:
    def reverseParentheses(self, s: str) -> str:
        s1 = []
        s2 = ""
        for i in s:
            if i=="(":
                s1.append(s2)
                s2=""
            elif i==")":s2 = s1.pop()+s2[::-1]
            else:s2+=i
        return s2