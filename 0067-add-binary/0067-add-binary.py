class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remenber = 0
        result = ""
        for i in range(max(len(a), len(b))):
            x = int(a[-1-i]) if i < len(a) else 0
            y = int(b[-1-i]) if i < len(b) else 0
            sum_ = x + y + remenber
            remenber = sum_ // 2
            result += str(sum_ % 2)

        if remenber:
            result += str(remenber)
        return result[::-1]