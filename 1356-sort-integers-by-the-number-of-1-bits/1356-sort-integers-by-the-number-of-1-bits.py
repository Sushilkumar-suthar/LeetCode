class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        buckets = [[] for _ in range(14)]

        for x in arr:
            bits = x.bit_count()
            buckets[bits].append(x)

        ans = []

        for bucket in buckets:
            bucket.sort()
            ans.extend(bucket)

        return ans