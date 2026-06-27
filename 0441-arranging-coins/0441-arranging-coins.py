class Solution:
    def arrangeCoins(self, n: int) -> int:
        c =0
        i = 1
        while n/i>=1:
            c+=1
            n-=i
            i+=1
        return c