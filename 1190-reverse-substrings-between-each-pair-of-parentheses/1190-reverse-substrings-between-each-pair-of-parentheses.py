class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        s1 = []
        s2 = ""
        while i<len(s):
            if s[i]=="(":
                s1.append(s2)
                s2=""
            elif s[i]==")":
                s2 = s1.pop()+s2[::-1]
            else:
                s2+=s[i]
            i+=1

        return s2
        