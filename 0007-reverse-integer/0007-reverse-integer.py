class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x:
            digit = x % 10
            x //= 10

            if rev > 214748364 or (
                rev == 214748364 and digit > (7 if sign == 1 else 8)
            ):
                return 0

            rev = rev * 10 + digit

        return sign * rev