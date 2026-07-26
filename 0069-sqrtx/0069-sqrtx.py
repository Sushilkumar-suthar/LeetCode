import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:return 0
        guess = x
        while abs(guess * guess - x) > 0.0001:
            guess = (guess + x / guess) / 2

        return math.floor(guess)