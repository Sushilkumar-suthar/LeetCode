class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        for i in word:
            if i.isupper():
                c+=1

        return c==len(word) or c==0 or (c==1 and word[0].isupper())