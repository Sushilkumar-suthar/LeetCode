class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def count_bits(n):
            count = 0

            while n > 0:
                n = n & (n - 1)
                count += 1

            return count

        result_a = count_bits(a)
        result_b = count_bits(b)

        if result_a >= result_b:
            return result_a * result_b

        return result_b // result_a