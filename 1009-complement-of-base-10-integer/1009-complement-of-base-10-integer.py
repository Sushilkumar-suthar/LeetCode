class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n^(2**n.bit_length())-1 if n>0 else 1