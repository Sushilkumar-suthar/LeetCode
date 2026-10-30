class Solution:
    def countMonobit(self, n: int) -> int:
        a = x = 1
        i = 1
        while x <= n:
            a += 1
            x += 1 << i
            i += 1
        return a
