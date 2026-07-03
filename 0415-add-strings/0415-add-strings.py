class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        carry = 0
        ans = ""

        for i in range(max(l1, l2) - 1, -1, -1):
            if l1 < l2:
                idx1 = i - (l2 - l1)
                n1 = ord(num1[idx1]) - ord('0') if idx1 >= 0 else 0
                n2 = ord(num2[i]) - ord('0')
            else:
                idx2 = i - (l1 - l2)
                n1 = ord(num1[i]) - ord('0')
                n2 = ord(num2[idx2]) - ord('0') if idx2 >= 0 else 0

            total = n1 + n2 + carry
            ans = chr(total % 10 + ord('0')) + ans
            carry = total // 10

        if carry:
            ans = chr(carry + ord('0')) + ans

        return ans