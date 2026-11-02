class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d = {
            0:0, 1:0,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0
        }
        while n>0:
            m = n%10
            # print(n,"m",m)
            d[m]+=1
            n=n//10

        s=0
        # print(d, s)
        for k,v in d.items():
            if v>0:
                s+=(k*v)
        return s