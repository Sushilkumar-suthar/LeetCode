class Solution:
    def sortByBits(self, arr):
        count = [0] * 15

        for x in arr:
            count[x.bit_count()] += 1

        buckets = [[] for _ in range(15)]

        for x in arr:
            buckets[x.bit_count()].append(x)

        ans = []

        for b in range(15):
            bucket = buckets[b]

            freq = [0] * 10001
            for x in bucket:
                freq[x] += 1

            for x in range(10001):
                if freq[x]:
                    ans.extend([x] * freq[x])

        return ans
