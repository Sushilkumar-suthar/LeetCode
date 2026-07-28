class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            s = 0

            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10

            n = s

        return n == 1
