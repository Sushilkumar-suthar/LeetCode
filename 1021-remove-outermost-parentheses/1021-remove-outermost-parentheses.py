class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        news = ""
        for i in s:
            if i == "(":
                if count != 0:
                    news+=i
                count +=1
            else:
                count -=1
                if count != 0:
                    news+=i
        return news
