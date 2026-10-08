class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        news = ""
        sp = 0
        index= 0
        for i in s:
            index+=1
            if i == "(":
                count+=1
                if sp==0:
                    sp=index
            else:
                count-=1

            if count ==0:
                news += s[sp:index-1]
                sp=0
            
        return news
