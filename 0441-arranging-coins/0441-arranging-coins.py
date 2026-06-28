class Solution:
    def arrangeCoins(self, n: int) -> int:
        c =0
        i = 1
        while ((i*(i+1))/2)<=n:
            c+=1
            # n-=i
            i+=1
        return c