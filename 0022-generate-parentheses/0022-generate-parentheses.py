class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(current, open, close):
            if open == n and close == n:
                result.append(current)
                return

            if open < n:
                dfs(current + "(", open + 1, close)

            if close < open:
                dfs(current + ")", open, close + 1)

        dfs("", 0, 0)

        return result