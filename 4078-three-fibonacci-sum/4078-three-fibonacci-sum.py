class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b = 0, 1

        while 2 * b <= n:
            if 2 * b == n:
                return True

            a, b = b, a + b

        return False