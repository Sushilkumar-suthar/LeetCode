
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        gains = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    gains[i] += 1

        min_price = min(price for _, price in items)

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            gain = gains[i]

            for c in range(budget, price - 1, -1):
                dp[c] = max(dp[c], dp[c - price] + gain)

        ans = 0

        for cost in range(budget + 1):
            extra = (budget - cost) // min_price
            ans = max(ans, dp[cost] + extra)

        return ans