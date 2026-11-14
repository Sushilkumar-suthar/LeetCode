class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)

        def sumSubarrayMax():
            stack = []
            total = 0

            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] < nums[i]):
                    mid = stack.pop()

                    left = mid - stack[-1] if stack else mid + 1
                    right = i - mid

                    total += nums[mid] * left * right

                stack.append(i)

            return total

        def sumSubarrayMin():
            stack = []
            total = 0

            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] > nums[i]):
                    mid = stack.pop()

                    left = mid - stack[-1] if stack else mid + 1
                    right = i - mid

                    total += nums[mid] * left * right

                stack.append(i)

            return total

        return sumSubarrayMax() - sumSubarrayMin()