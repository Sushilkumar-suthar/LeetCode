class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(x):
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count

        return sorted(arr, key=lambda x: (count_bits(x), x))