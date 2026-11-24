class Solution:
    def maxLength(self, nums: List[int]) -> int:
        a = len(nums)
        b = 1

        for c in range(a):
            d = 1
            e = 0
            f = 1

            for g in range(c, a):
                d *= nums[g]
                e = gcd(e, nums[g])
                f = lcm(f, nums[g])

                if d == e * f:
                    b = max(b, g - c + 1)

        return b